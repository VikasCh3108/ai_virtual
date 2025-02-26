from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging
from datetime import datetime
from typing import List

from app.core.database import get_db, engine
from app.models.interaction import Base, Interaction
from app.schemas.interaction import InteractionCreate, InteractionResponse
from app.services.nlp_service import NLPService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Voice Assistant API")
nlp_service = NLPService()

@app.post("/process", response_model=InteractionResponse)
async def process_input(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    try:
        # Log the incoming request
        logger.info(f"Received input: {interaction.user_input}")

        # Process the input using NLP service
        intent, response = nlp_service.process_input(interaction.user_input)

        # Create database record
        db_interaction = Interaction(
            user_input=interaction.user_input,
            intent=intent,
            response=response
        )
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)

        # Log the response
        logger.info(f"Processed intent: {intent}, Response: {response}")

        return db_interaction
    except Exception as e:
        logger.error(f"Error processing input: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/interactions", response_model=List[InteractionResponse])
async def get_interactions(db: Session = Depends(get_db)):
    try:
        return db.query(Interaction).all()
    except Exception as e:
        logger.error(f"Error retrieving interactions: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

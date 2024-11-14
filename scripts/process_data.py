from src.data.processor import DataProcessor
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/processing.log'),
            logging.StreamHandler()
        ]
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        processor = DataProcessor()
        processor.process_all_wallets()
        logger.info("Processing complete")
        
    except Exception as e:
        logger.error(f"Error in data processing: {str(e)}")

if __name__ == "__main__":
    main()
import os
import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """
    Handles EC2 instance start/stop requests
    """
    logger.info(f"Received event: {event}")

    # Get instance IDs from environment variables
    instance_ids = os.environ.get('INSTANCE_IDS', '')
    
    if not instance_ids:
        logger.error("INSTANCE_IDS environment variable is missing or empty")
        return {"status": "error", "message": "No instance IDs configured"}

    instance_ids = instance_ids.split(',')

    # Validate event payload
    if not isinstance(event, dict) or 'action' not in event:
        logger.error("Missing or invalid 'action' in event")
        return {"status": "error", "message": "Missing 'action' in request"}

    action = str(event.get('action', '')).strip().lower()

    if action not in ["start", "stop"]:
        logger.error(f"Invalid action specified: {action}")
        return {"status": "error", "message": "Invalid action specified. Use 'start' or 'stop'"}

    try:
        if action == "start":
            response = ec2.start_instances(InstanceIds=instance_ids)
            logger.info(f"Starting instances: {instance_ids}")
            return {
                "status": "success",
                "message": f"Instances {instance_ids} starting",
                "response": response
            }
        
        elif action == "stop":
            response = ec2.stop_instances(InstanceIds=instance_ids)
            logger.info(f"Stopping instances: {instance_ids}")
            return {
                "status": "success",
                "message": f"Instances {instance_ids} stopping",
                "response": response
            }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"status": "error", "message": str(e)}

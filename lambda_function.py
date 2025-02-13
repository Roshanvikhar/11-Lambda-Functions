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
    # Get instance IDs from environment variables
    instance_ids = os.environ['INSTANCE_IDS'].split(',')
    
    # Validate instance IDs
    if not instance_ids or instance_ids == ['']:
        return {"status": "error", "message": "No instance IDs configured"}
    
    try:
        # Determine action from event payload
        action = event.get('action', '').lower()
        
        if action == 'start':
            response = ec2.start_instances(InstanceIds=instance_ids)
            logger.info(f"Starting instances: {instance_ids}")
            return {
                "status": "success",
                "message": f"Instances {instance_ids} starting",
                "response": response
            }
            
        elif action == 'stop':
            response = ec2.stop_instances(InstanceIds=instance_ids)
            logger.info(f"Stopping instances: {instance_ids}")
            return {
                "status": "success",
                "message": f"Instances {instance_ids} stopping",
                "response": response
            }
            
        else:
            return {"status": "error", "message": "Invalid action specified. Use 'start' or 'stop'"}

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"status": "error", "message": str(e)}
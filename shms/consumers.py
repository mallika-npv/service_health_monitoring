# consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import service

class ServiceStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            # Fetch all services from the database
            services = service.objects.all()

            # Check the time field for each service and update status accordingly
            for s in services:
                temp = s.time
                if s.time > 0:
                    s.time -= 1
                else:
                    s.status = not s.status
                    s.time = temp  # Reset the time

                # Save the updated status and time
                s.save()

                # Send real-time update to the connected client
                await self.send(text_data=json.dumps({
                    'service_name': s.name,
                    'status': s.status,
                }))

            # Wait for n seconds before the next update (adjust this value as needed)
            await asyncio.sleep(s.time)

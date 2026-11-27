from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal


app = FastAPI(
    title="NexusOps API",
    description="AI-Powered IT Operations Plataform",
    version="0.1.0"
)

class DeviceCreate(BaseModel):
    name: str
    type: Literal["OLT", "Switch", "Router", "Server", "Firewall", "Access Point"]
    status: Literal["online", "ofline", "maintence"] 

class DeviceUpdate(BaseModel):
    name: str | None = None
    type: Literal["OLT", "Switch", "Router", "Server", "Firewall", "Access Point"] | None = None
    status: Literal["online", "offline", "maintenance"] | None = None



@app.get("/")
def health_check():
    return {
        "status": "healty"
    }

@app.get("/devices")
def devices_check():
    return[
        {
            "id": 1,
            "name": "OLT-01",
            "type": "OLT",
            "status": "online"
        },
        {
            "id": 2,
            "name": "SWITCH-01",
            "type": "Switch",
            "status": "offline",
        },
        {
            "id": 3,
            "name": "ROUTER-01",
            "type": "router",
            "status": "online",
        }
    ]


devices =[
            {
                "id": 1,
                "name": "OLT-01",
                "type": "OLT",
                "status": "online"
            },
            {
                "id": 2,
                "name": "SWITCH-01",
                "type": "Switch",
                "status": "offline",
            },
            {
                "id": 3,
                "name": "ROUTER-01",
                "type": "router",
                "status": "online",
            }
        ]

@app.get("/devices/online")
def devices_online():
    online_devices = []

    for device in devices:
        if device["status"] == "online":
            online_devices.append(device)
    return online_devices

@app.get("/devices/offline")
def devices_offline():
    offline_devices = []

    for device in devices:
        if device["status"] == "offline":
            offline_devices.append(device)
    return offline_devices

@app.get("/devices/summary")
def devices_summary():
    total = len(devices)
    offline = 0
    online = 0

    for device in devices:
        if device["status"] == "online":
            online = online + 1
        elif device["status"] == "offline":
            offline = offline + 1

    if total == 0:
        avaiability = 0
    else:
        avaiability = round((online / total) * 100, 2)

            
    return{
        "total": total,
        "online": online,
        "offline": offline,
        "availability": avaiability
    }

@app.post("/devices", status_code=201)
def create_device(device: DeviceCreate):

    new_device = {
        "id": max((d["id"] for d in devices), default=0) + 1,
        "name": device.name,
        "type": device.type,
        "status": device.status
    }

    devices.append(new_device)

    return new_device

@app.get("/devices/{device_id}")
def get_device(device_id: int):

    for device in devices:
        if device_id == device["id"]:
            return device

    raise HTTPException(
        status_code= 404,
        detail="Device not found"
    )

@app.put("/devices/{device_id}")
def update_device(device_id: int, updated_device: DeviceCreate):

    for device in devices:
        if device["id"] == device_id:
            device["name"] = updated_device.name
            device["type"] = updated_device.type
            device["status"] = updated_device.status

            return device

    raise HTTPException(
        status_code=404,
        detail="Device not found"
    )


@app.delete("/devices/{device_id}")
def delete_device(device_id: int):

    for device in devices:
        if device["id"] == device_id:
            devices.remove(device)

            return{
                "message": "Device deleted successfuly"
            }

    raise HTTPException(
        status_code=404,
        detail="Device not found"
    )


@app.patch("/devices/{device_id}")
def patch_device(device_id: int, updated_device: DeviceUpdate):

    for device in devices:
        if device["id"] == device_id:

            updated_data = updated_device.model_dump(exclude_none=True)
            device.update(updated_data)

            return device

    raise HTTPException(
        status_code=404,
        detail = "Device not found"
    )
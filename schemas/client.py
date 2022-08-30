from datetime import datetime


def clientEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "fullname":str(item["fullname"]),
        "phonenumber":str(item["phonenumber"]),
        "isValidate":bool(item["isValidate"]),
        "email":str(item["email"]),
        
        

    }

def cEntity(item) -> dict:
    return {
        
        "fullname":str(item["fullname"]),
        "phonenumber":str(item["phonenumber"]),
        "isValidate":bool(item["isValidate"]),
        "email":str(item["email"]),
        

    }

def clientsEntity(entity)->list:
    return [clientEntity(item) for item in entity]

def parkEntity(item)-> dict:
    return {
        "id":str(item["_id"]),
        "parkname":str(item["parkname"]),
        "parkaddress":str(item["parkaddress"]),
        "parkinmaps":list(item["maps"]),
        "city":str(item["city"]),
        "surface":float(item["surface"]),
        "note":float(item["note"])
        

    }
def parksEntity(entity)->list:
    return [parkEntity(item) for item in entity]

def spotEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "spotcode":str(item["spotcode"]),
        "spottype":str(item["spottype"]),
        "spotisreserved":bool(item["spotisreserved"]),
        "parkid":str(item["parkid"]),


    }
def spotsEntity(entity)->list:
    return [spotEntity(item) for item in entity]

def carEntity(item)->dict:
    return{
     "id":str(item["_id"]),
     "carmatricule":str(item["carmatricule"]),
     "cartype":str(item["cartype"]),
     "carmark":str(item["carmark"]),
     "clientid":str(item["clientid"])
    }
def carsEntity(entity)->list:
    return [carEntity(item) for item in entity]


def reviewEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "note":float(item["note"]),
        "parkid":str(item["parkid"]),
        "clientid":str(item["clientid"]),
        "comment":str(item["comment"])
    }
def reviewsEntity(entity)->list:
    return [reviewEntity(item) for item in entity]

def reservationEntity(item)->dict:
    return {
    "clientId":str(item["clientId"]),
    "spotId":str(item["spotId"]),
    "startDate": datetime(item["startDate"]),
    "endDate": datetime(item["endDate"]),
    
    "value":float(item["value"]),
    "isPaid": bool(item["isPaid"])
    }

def resrvationsEntity(entity)->list:
    return [resrvationsEntity(item) for item in entity]

def pricingEntity(item)->dict:
    return{
        "pricingId": str(item["_id"]),
        "normalPricing": str(item["normalPricing"]),
        "extraPricing": str(item["extraPricing"]),
        "parkId": str(item["parkId"]),

    }
def pricingsEntity(entity)->list:
    return [pricingEntity(item) for item in entity]

def bookingEntity(item)->dict:
    return{
        "id": str(item["_id"]),
        "clientId":str(item["clientId"]),
        "spotId":str(item["spotId"]),
        "startDate":str(item["startDate"]),
        "endDate":str(item["endDate"]),
        "value":float(item["value"]),
        "isPaid":bool(item["isPaid"]),
        "parkName":str(item["parkName"]),
        "spotType":str(item["spotType"]),
        "parkId":str(item["parkId"]),
        "carNumber":str(item["carNumber"]),

    }
def bookingsEntity(entity)->list:
    return [bookingEntity(item) for item in entity]
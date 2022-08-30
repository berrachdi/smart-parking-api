from calendar import day_abbr
from http.client import CannotSendRequest
import json
from turtle import end_fill

import io
import qrcode
from starlette.responses import StreamingResponse

from unittest import result
from fastapi import APIRouter
from models.client import Client
from models.park import Park
from models.spot import Spot
from models.car import Car
from models.pricing import Pricing
from models.review import Review
from models.reservation import Reservation
from config.db import conn
from schemas.client import bookingsEntity,bookingEntity,pricingEntity,reviewEntity,reviewsEntity,carEntity,carsEntity,clientEntity, clientsEntity,parkEntity,parksEntity,spotEntity,spotsEntity
from bson.objectid import ObjectId
from .secureAuth import Hasher
from datetime import datetime

clientAPI = APIRouter()
cashless_db = conn['cashless-app']

@clientAPI.get('/clients')
async def find_all_client():
    clients = cashless_db['client']
    return clientsEntity(conn.cashless_db.clients.find())

@clientAPI.get('/client')
async def find_one_client(id):
    clients = cashless_db['client']
    return clientEntity( conn.cashless_db.clients.find_one({ "_id":ObjectId(id)} )  )

@clientAPI.post('/signup')
async def add_client(client: Client):
    clients = cashless_db['client']
    #print(dict(client)['password'])
    #dict(client)['password'] = Hasher.get_password_hash(dict(client)['password'])
    result = conn.cashless_db.clients.insert_one(dict(client))
    if result == None:
        return {"message": "Sorry, somthing happened wrong, please try again"}
    else:
        return {"message": "Signup Successfully"}

@clientAPI.get('/login')
async def login_client(email: str,password: str):
   
    clients = cashless_db['client']
    result = conn.cashless_db.clients.find_one({"password": password, "email": email})
    
    if result == None:
        return {"message": "email or password incorrect"}  
    else:
        return clientEntity(result)

@clientAPI.put('/clients')
async def update_client(id, client:Client):
    clients = cashless_db['client']
    conn.cashless_db.clients.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(client)
    })

    return clientEntity(conn.cashless_db.clients.find_one({"_id":ObjectId(id)}))

@clientAPI.delete('/clients')
async def delete_client(id):
    clients = cashless_db['client']
    result = conn.cashless_db.clients.find_one_and_delete({"_id":ObjectId(id)})
    

    return clientEntity(result)

# Api routers for Park
@clientAPI.get('/parks')
async def find_all_client():
    parks = cashless_db['park']
    return parksEntity(conn.cashless_db.parks.find())

@clientAPI.post('/parks')
async def add_park(park:Park):
    parks = cashless_db['park']
    conn.cashless_db.parks.insert_one(dict(park))
    return parksEntity(conn.cashless_db.parks.find())

@clientAPI.get('/park')
async def find_park_by_id(id):
     parks = cashless_db['park']
     result = conn.cashless_db.parks.find_one({"_id": ObjectId(id)})
     if result is not None:
        return {"message":"park founded","data":parkEntity(result)}
     else:
        return {"message": "park not found"}

@clientAPI.get('/parksearch')
async def find_park_by_name(q:str):
     parks = cashless_db['park']
     result = conn.cashless_db.parks.find({ 'parkname' : { '$regex' : q, '$options' : 'i' } })
     if result is not None:
        return parksEntity(result)
     else:
        return {"message": "park not found"}

@clientAPI.get('/parkcity')
async def find_park_by_city(city:str):
     parks = cashless_db['park']
     result = conn.cashless_db.parks.find({ 'city' : { '$regex' : city, '$options' : 'i' } })
     if result is not None:
        return parksEntity(result)
     else:
        return {"message": "park not found"}

@clientAPI.put('/parks')
async def update_park(id, park:Park):
    parks = cashless_db['park']
    conn.cashless_db.parks.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(park)
    })

    return clientEntity(conn.cashless_db.parks.find_one({"_id":ObjectId(id)}))

@clientAPI.delete('/parks')
async def delete_park(id):

    parks = cashless_db['park']
    result = conn.cashless_db.parks.find_one_and_delete({"_id":ObjectId(id)})
    return result

#api routers for spot
@clientAPI.post('/spots')
async def add_spot(spot: Spot):

    spots = cashless_db['spot']
    result = conn.cashless_db.spots.insert_one(dict(spot))
    return spotsEntity(conn.cashless_db.spots.find())

@clientAPI.put('/spots')
async def update_spot(id, spot: Spot):
    
    spots = cashless_db['spot']
    conn.cashless_db.spots.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(spot)
    })
    return clientEntity(conn.cashless_db.spots.find_one({"_id":ObjectId(id)}))

@clientAPI.delete('/spots')
async def delete_spot(id):

    
    spots = cashless_db['spot']
    result = conn.cashless_db.spots.find_one_and_delete({"_id":ObjectId(id)})
    return result

@clientAPI.get('/spot')
async def find_spot_by_id(id):
    spots = cashless_db['spot']
    result = conn.cashless_db.spots.find_one({"_id":ObjectId(id)})
    if result == None:
        return {"message": "No spot found"}
    else:
        return spotEntity(result)

@clientAPI.get('/spots')
async def find_all_park_spot(parkid):
    spots = cashless_db['spot']
    result = conn.cashless_db.spots.find({"parkid":parkid})
    print("hello")
    if result == None:
        return {"message": "No spot found for this park"}
    else:
        return spotsEntity(result)

@clientAPI.get('/spotsnotreserved')
async def find_all_park_spot_not_reserved(parkid):

    
    spots = cashless_db['spot']
    result = conn.cashless_db.spots.find({"parkid":parkid,"spotisreserved":False})
    if result == None:
        return {"message": "No spot disponible found for this park"}
    else:
        return spotsEntity(result)


@clientAPI.post('/cars')
async def add_car(car:Car):
    cars = cashless_db['car']
    result = conn.cashless_db.cars.insert_one(dict(car))
    return carsEntity(conn.cashless_db.cars.find())

@clientAPI.put('/cars')
async def update_car(id, car:Car):
    cars = cashless_db['car']
    conn.cashless_db.cars.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(car)
    })

    return carEntity(conn.cashless_db.cars.find_one({"_id":ObjectId(id)}))

@clientAPI.delete('/parks')
async def delete_car(id):

    cars = cashless_db['car']
    result = conn.cashless_db.cars.find_one_and_delete({"_id":ObjectId(id)})
    return result

@clientAPI.get('/cars')
async def get_cars():
    cars = cashless_db['car']
    results = conn.cashless_db.cars.find({"_id":ObjectId(id)})
    return carsEntity(results)

@clientAPI.post('/reviews')
async def add_review(review:Review):
    reviews = cashless_db['review']
    #add the review to the park
    result = conn.cashless_db.reviews.insert_one(dict(review))

    #get reviews
    result2 = conn.cashless_db.reviews.find({"parkid":dict(review)["parkid"]})

    #calculate the note
    note = 0
    listReviews = reviewsEntity(result2)
     
    for review in listReviews:
        note = note + review['note']
    
    note = note/len(listReviews)

    #update the park note
    parks = cashless_db['park']
    id = dict(review)["parkid"]
    
    park = conn.cashless_db.parks.find_one({"_id": ObjectId(id)})
    parkupdated = dict(park)
    print(parkupdated)
    parkupdated["note"]=round(note,1)
    print(parkupdated)
    conn.cashless_db.parks.find_one_and_update({"_id":ObjectId(id)},{
        "$set": parkEntity(parkupdated)
    })

    return parkEntity(conn.cashless_db.parks.find_one({"_id":ObjectId(id)}))







    return reviewsEntity(conn.cashless_db.reviews.find())

@clientAPI.get('/reviews')
async def get_note_for_park(parkid):
     reviews = cashless_db['review']
     result = conn.cashless_db.reviews.find({"parkid":parkid})
     note = 0
     listReviews = reviewsEntity(result)
     
     for review in listReviews:
        note = note + review['note']
        print(note)
    
     return {"note": note/len(listReviews)}


@clientAPI.post('/booking')
async def add_booking(reservation:Reservation):
    print(reservation)
    
    bookings = cashless_db['booking']
    #Calcule the delay
    reservation = dict(reservation)
    print(reservation['startDate'])
    #startDate = reservation['startDate'].replace("T"," ").replace("Z","").replace("-","/").replace("2022","22")
    #endDate = reservation['endDate'].replace("T"," ").replace("Z","").replace("-","/").replace("2022","22")
    startDate = reservation['startDate']
    endDate = reservation['endDate']
    
    duration_on_minutes = (endDate-startDate)
    print(duration_on_minutes.seconds/60)
    duration_on_hour = duration_on_minutes.seconds/60
    duration_on_hour = duration_on_hour/60
    print(duration_on_hour)

    #Calcule the price 
    pricings = cashless_db['pricing']
    spots = cashless_db['spot']
    #print(reservation['spotId'])
    spotResult = conn.cashless_db.spots.find_one({"_id":ObjectId(reservation['spotId'])})
    spotResultDict = spotEntity(spotResult)
    #print(spotResultDict['parkid'])
    pricingResult = conn.cashless_db.pricings.find_one({"parkId":spotResultDict['parkid']})
    pricingResultDict = pricingEntity(pricingResult)
    #print(pricingResultDict['normalPricing'])
    json_pricing = pricingResultDict['normalPricing'].replace("'",'"')
    json_pricing_object = json.loads(json_pricing)
    print(type(duration_on_hour))
    if duration_on_hour <=2:
        price = int(json_pricing_object['2'])
    elif duration_on_hour <=4:
        price = int(json_pricing_object['4'])
    elif duration_on_hour <=6:
        price = int(json_pricing_object['6'])
    elif duration_on_hour <=12:
        price = int(json_pricing_object['12'])
    else:
        price = int(json_pricing_object['24'])
    
    reservation['value'] = price 
    reservation['isPaid'] = False
    spotResultDict['spotisreserved'] = True

    resultBooking = conn.cashless_db.bookings.insert_one(reservation)
    updateSpot = conn.cashless_db.spots.find_one_and_update({"_id":ObjectId(spotResultDict["id"])},{"$set":spotResultDict})
    
    return {"message":"Spot is reserved but not confirmed yet"}
    


    #convert 

    #result = conn.cashless_db.pricings.find({"parkid":reservation['parkid']})
    #resultone = pricingEntity(result)
    

    #result = conn.cashless_db.booking.insert_one(dict(reservation))
    return {"message": "the reservation added successfully.","delay":duration_on_minutes}


@clientAPI.get('/bookingcheck')
async def bookingcheck(parkId,startDate,endDate,spotType):
     print(startDate)
     spots = cashless_db['spot']
     startd = startDate.replace("T"," ").replace("Z","").replace("-","/").replace("2022","22")
     startd = startd.split(".")[0]
     endd = endDate.replace("T"," ").replace("Z","").replace("-","/").replace("2022","22")
     endd = endd.split(".")[0]
     startd_format = datetime.strptime(startd, '%y/%m/%d %H:%M:%S')
     endd_format = datetime.strptime(endd, '%y/%m/%d %H:%M:%S')
     duration_on_seconds = endd_format-startd_format
     

     #find a not reserved spot in park identified by parkId between a startDate and endDate
     spotsNotReserved = conn.cashless_db.spots.find({"parkid":parkId,"spotisreserved":False,"spottype":spotType})
     spotSearchResult = spotsEntity(spotsNotReserved)
     if len(spotSearchResult) == 0:
        return {"message": "All spots in this park are reserved."}
     else:
        return {"message":"There are "+str(len(spotSearchResult))+" spaces available in this park","data":spotSearchResult}
     #spotsReserved but will be termined at startDate
     #spotsReservedButUssabl = conn.cashless_db.spots.find({"parkid":parkId,"spotisreserved":True,"spottype":spotType})
     #spotsr = spotsEntity(spotsReservedButUssabl)


     
     
@clientAPI.post('/pricing')
async def add_pricing(pricing: Pricing):
    pricings = cashless_db['pricing']
    result = conn.cashless_db.pricings.insert_one(dict(pricing))
    return {"message": "the pricing was successfully added."}


@clientAPI.get('/booking')
async def get_booking(clientId):
     bookings = cashless_db['booking']
     results = conn.cashless_db.bookings.find({"clientId":clientId})
     
     return {"data":bookingsEntity(results)}

     

@clientAPI.get('/eticket')
async def get_ticket(bookingId):

    bookings = cashless_db['booking']
    result = conn.cashless_db.bookings.find_one({"_id":ObjectId(bookingId)})
    booking = bookingEntity(result)
    img = qrcode.make(booking)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0) # important here!
    return StreamingResponse(buf, media_type="image/jpeg")


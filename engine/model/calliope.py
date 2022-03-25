from datetime import datetime

from engine.capulet_engine import CapuletEngine

class CarFactory(object):
	def __init__(self):
		self.engine=Engine()
		self.battery=Battery()
		self.car=Car()
	def create_calliope(current_date,last_service_date,current_mileage,last_service_mileague):
        #order sensitive
        capulet = CapuletEngine(current_mileage,last_service_mileague);
        nubbin = NubbinBattery(last_service_date,current_date);     
        calliope = Car(capulet,nubbin);
        return calliope;
        
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileague):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileague);
        nubbin = NubbinBattery(last_service_date,current_date);    
        glissade= Car(willoughby,nubbin);
        return glissade();
        
    def create_palindrome(current_date,last_service_date,warning_light_on):
        stern = SternmanEngine(current_date,last_service_date,warning_light_on);
        nubbin = NubbinBattery(last_service_date,current_date);    
        palindrome = Car(stern,nubbin)
        return palindrome;
         
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileague):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileague);
        nubbin = NubbinBattery(last_service_date,current_date); 
        rorscheache = Car(willoughby,nubbin)
        return rorscheache;
         
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileague):
        capulet = CapuletEngine(current_mileage,last_service_mileague);
        nubbin = NubbinBattery(last_service_date,current_date);     
        thovex = Car(capulet,nubbin);
        return  thovex;

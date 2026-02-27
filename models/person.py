class Person:
    def __init__(self, id, name, age, country, gaverment, gender, job):
        self._id = id
        self._name = name
        self._age = age
        self._country = country
        self._gaverment = gaverment
        self._gender = gender
        self._job = job
  
    def get_id(self): 
        return self._id

    def get_name(self): 
        return self._name    
    
    def get_age(self):
        return self._age
        
    def get_country(self):
        return self._country
        
    def get_gaverment(self):
        return self._gaverment
        
    def get_gender(self):
        return self._gender
        
    def get_job(self):
        return self._job

    def to_dict(self):
        return {
            "id":self._id,
            "name":self._name,
            "age":self._age,
            "country":self._country,
            "gaverment":self._gaverment,
            "gender":self._gender,
            "job":self._job
        }
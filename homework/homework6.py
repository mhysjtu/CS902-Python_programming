class Country:
    def __init__(self,name,population,area):
        self.name=name
        self.population= population
        self.area=area

    def is_larger(self,obj):
        if self.area > obj.area:
            return True
        else:
            return False

    def population_density(self):
        return float(self.population) / self.area

    def __str__(self):
        return self.name+" has a population of "+str(self.population)+" and is "+str(self.area)+" square km. "

    def __repr__(self):
        return "Country('"+self.name+"',"+str(self.population)+","+str(self.area)+")"

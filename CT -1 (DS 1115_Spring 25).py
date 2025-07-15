class Model:
    def __init__(self,name:str,accuracy_score:float,execution_time:float):
        self.name=name
        self.accuracy_score=accuracy_score
        self.execution_time=execution_time
    
    def update_accuracy(self,score):
        self.accuracy_score=score
        
    def update_execution_time(self,time):
        self.execution_time=time
        
class Team:
    def __init__(self,name,model:Model):
        self.name=name
        self.model=model
        
    def assign_model(self,model:Model):
        self.model=model
        
    def get_model_performance(self):
        return (self.model.accuracy_score, self.model.execution_time)

def compare_model(team1:Team,team2:Team):
    team1_per=team1.get_model_performance()
    team2_per=team2.get_model_performance()
    
    if team1_per[0]==team2_per[0]:
        if team1_per[1]<team2_per[1]:
            print(f"Team {team1.name} wins with a model accuracy of {team1_per[0]}%!")
        else:
            print(f"Team {team2.name} wins with a model accuracy of {team2_per[0]}%!")
    elif team1_per[0]>team2_per[0]:
        print(f"Team {team1.name} wins with a model accuracy of {team1_per[0]}%!")
    else:
        print(f"Team {team2.name} wins with a model accuracy of {team2_per[0]}%!")
        
model1 = Model("Model A", 92.5, 1.2)
model2 = Model("Model B", 90.8, 1.0)

team1 = Team("Alpha", model1)
team2 = Team("Beta", model2)

compare_model(team1, team2)


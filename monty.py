#!/usr/bin/env python
import random
import sys

class MontyPlayer(object):

    def __init__(self,door_count,switch=False):
        self.switch=switch
        #per-player list of doors
        self.doors=[]

        for i in range(0,door_count):
            self.doors.append(MontyDoor())
        winning_door=self.doors[random.randint(0,len(self.doors)-1)]
        winning_door.set_winning()
        
        self.choice=self._choose_door(self.doors)
        
        #player choice not available for revealing or choosing again
        self.doors.remove(self.choice)
        
    def wins_prize(self):
        if self.choice.outcome=="prize":
            return True
        else:
            return False
    
    def _choose_door(self,doors):
        return doors[random.randint(0,len(doors)-1)]
    
    def door_revealed(self,door):
        if not door in self.doors:
            raise Exception("Invalid door number.")
        self.doors.remove(door)
        if self.switch:
            #With three doors total, at this point there should be only one door remaining, which we will now choose.
            self.choice=self._choose_door(self.doors)
            self.doors.remove(self.choice)

class MontyDoor(object):

    def __init__(self):
        self.outcome="goat"

    def set_winning(self):
        self.outcome="prize"

class MontyGame(object):
    DOOR_COUNT=3
            
    def __init__(self,trials):
        self.switch_win_tally=0
        self.non_switch_win_tally=0
        for i in range(0,trials):
            players=[]
            switch_player=MontyPlayer(self.DOOR_COUNT,switch=True)
            players.append(switch_player)
            non_switch_player=MontyPlayer(self.DOOR_COUNT,switch=False)
            players.append(non_switch_player)
            self._run_trial(players)
            if switch_player.wins_prize():
                self.switch_win_tally+=1
            if non_switch_player.wins_prize():
                self.non_switch_win_tally+=1
                
    def _run_trial(self,players):
        for p in players:
            for door in p.doors:
                if door.outcome=="goat":
                    p.door_revealed(door)
                    break
            

        
def main(trials):
    game=MontyGame(trials)
    print("Trials: %d" % trials)
    print("Switching player wins: %d" % game.switch_win_tally)
    print("Non-switching player wins: %d" % game.non_switch_win_tally)

if __name__ == '__main__':
    try:
        trials=int(sys.argv[1])
    except:
        trials=1000
    main(trials)

        
            
        
    
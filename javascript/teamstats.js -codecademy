// We want to create, retrieve, and add information about your favorite sports team. Basketball, soccer, tennis, or water polo, you pick it. It’s your job to create data using the JavaScript data structures at your disposal: arrays and objects.
// After we create these data structures in this project, feel free to challenge yourself to gain insights from them. For example, you might want to get the total number of games your team has played, or the average score of all of their games.

const team = {
    _players: [
      {
        firstName: 'Alice',
        lastName: 'Ansible',
        age: 29
      },
      {
        firstName: 'Bethany',
        lastName: 'Bethesda',
        age: 39
      },
      {
        firstName: 'Candice',
        lastName: 'Compaq',
        age: 49
        }
    ],
    _games: [
      {
        opponent: 'Aloes',
        teamPoints: 10,
        opponentPoints: 5
      },
      {
        opponent: 'Bonsais',
        teamPoints: 20,
        opponentPoints: 30
      },
      {
        opponent: 'Cactuses',
        teamPoints: 10,
        opponentPoints: 5
      }
    ],
    get players() {
      return this._players;
    },
    get games() {
      return this._games;
    },
    addPlayer(firstName, lastName, age) {
      let player = {
        firstName: firstName, 
        lastName: lastName, 
        age: age
      };
      this.players.push(player);
    },
      addGame(opponent, teamPoints, opponentPoints) {
      let game = {
        opponent: opponent, 
        teamPoints: teamPoints, 
        opponentPoints: opponentPoints
      };
      this.games.push(game);
    }
  }

  team.addPlayer('Steph', 'Curry', 28);
  team.addPlayer('Lisa', 'Leslie', 44);
  team.addPlayer('Bugs', 'Bunny', 76);
  
  console.log(team._players);
  
  team.addGame('Dahlias', 15, 25);
  team.addGame('Eggplants', 30, 40);
  team.addGame('Ferns', 5, 15);
  
  console.log(team._games);

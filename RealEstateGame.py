
class Spaces:
    """This class creates an object for each space (property) on the board.  It includes the name of the space,
    rent, cost to purchase it, and who it is owned by if it is owned, otherwise it has None for the owner"""

    def __init__(self, name, rent):
        """Takes two parameters, name of the space and rent. Initializes data members to private data members"""
        self._rent = rent
        self._name = name
        self._owned_by = None #initializes owned by to None
        self._purchase_price = rent * 5 #initializes the purchase price to 5 times the rent

    def set_owned_by(self, name):
        """Sets the properties owned by when someone purchases a property or loses a property due to have a zero
        account balance"""
        self._owned_by = name
        return self._owned_by

    def get_owned_by(self):
        """Returns the name of the owner of the property or None if no one owns the property"""
        return self._owned_by

    def get_purchase_price(self):
        """Returns the purchase price for the property"""
        return self._purchase_price

    def get_rent(self):
        """Returns the amount of rent due when someone lands on a property that is owned by someone else"""
        return self._rent

    def get_name(self):
        """Returns the name of the property"""
        return self._name


class RealEstateGame:
    """This class contains the methods to play the Real Estate game"""

    def __init__(self):
        self._dictionary_of_spaces = {}  # a dictionary of Spaces objects with 0 being "GO" and 1 being space 1
        self._player_list = [] #a list of lists of players and their information
        self._players_added = [] #list of names of players added to the game

    def create_spaces(self, amount_of_money_go, array_of_rent=[]):
        """Creates 25 spaces total using the Spaces class and assigns them to the dictonary_of_spaces. Key value 0 is
        assigned as the 'GO' space and its value is the value passed as a parameter.
        Key 1 is assigned as the first name in list of names with the rent value of the first value in the array passed
        as a parameter"""
        list_of_names = ["Wyoming", "Vermont", "Alaska", "North Dakota", "South Dakota", "Delaware",
                         "Rhode Island", "Montana", "Hawaii", "Idaho", "Nebraska", "Alabama", "Colorado", "Arizona",
                         "Michigan", "North Carolina", "Georgia", "Ohio", "Illinois", "Pennsylvania",
                         "New York", "Florida", "Texas", "California"]
        x = 0
        y = 0
        l = 1
        self._dictionary_of_spaces[0] = "GO", amount_of_money_go
        for name in list_of_names:
            self._dictionary_of_spaces[l] = Spaces(list_of_names[x], array_of_rent[y])
            l += 1
            x += 1
            y += 1

    def create_player(self, player_name, initial_account_balance):
        """Takes players name and initial account balance as parameter.
        Checks to see if player name has already been added. If not, it adds players name, current space number of 0,
        and initial account balance to the player_info_list.  It then adds that player info list to the player list.
        The player list will contain each player's player_info_list"""
        player_info_list = []
        current_space_number = 0
        name = player_name
        account_balance = initial_account_balance
        if name in self._players_added:
            return print("A player with the same name has already been added")
        else:
            self._players_added.append(name)
            player_info_list.append(name)
            player_info_list.append(current_space_number)
            player_info_list.append(account_balance)
            self._player_list.append(player_info_list)

    def get_player_account_balance(self, players_name):
        """returns the players account balance"""
        for player in self._player_list:
            if players_name == player[0]:
                print(players_name, "'s balance is:", player[2])
                return player[2]

        print("Player not found")

    def set_player_account_balance(self, players_name, cost):
        """Sets a players balance.  This is used for purchasing a space."""
        for player in self._player_list:
            if players_name == player[0]:
                player[2] -= cost
                print(players_name, "'s new balance is", player[2])

    def pass_go(self, players_name):
        """This method adds money to the players account when they pass or land on go"""
        for player in self._player_list:
            if players_name == player[0]:
                player[2] += self._dictionary_of_spaces[0][1]
                print(players_name, "passed go. You collect", self._dictionary_of_spaces[0][1])

    def get_player_current_position(self, players_name):
        """gets the players current position"""
        for player in self._player_list:
            if players_name == player[0]:
                print(players_name, "'s current position is:", player[1])
                return int(player[1])
        print("Player not found")

    def set_player_current_position(self, players_name, spaces_to_move):
        """Sets player's current position. If the player passes space 24, it calls the pass go method and
         resets the players position to either 0 for GO space or the single digit number the player is now on"""
        for player in self._player_list:
            if players_name == player[0]:
                player[1] += spaces_to_move
                if player[1] == 25:
                    player[1] = 0
                    self.pass_go(players_name)
                if player[1] > 25:
                    self.pass_go(players_name)
                    player[1] -= 25

    def buy_space(self, players_name):
        """If a space is not owned by another player and the player that is passed as a parameter's account balance
        is higher than the purchase price, this method will deduct the purchase price from the account balance,
        set the owner to the player, and it will return True. Otherwise, it will return False."""
        balance = self.get_player_account_balance(players_name)
        current_position = self.get_player_current_position(players_name)
        owned_by = self._dictionary_of_spaces[current_position].get_owned_by()
        property_name = self._dictionary_of_spaces[current_position].get_name()
        cost = self._dictionary_of_spaces[current_position].get_purchase_price()

        if balance > cost and owned_by == None:
            print("The cost of", property_name, "is", cost)
            self._dictionary_of_spaces[current_position].set_owned_by(players_name)
            self.set_player_account_balance(players_name, cost)
            print(players_name, "has purchased", property_name)

            return True

        else:
            return False

    def move_player(self, players_name, spaces_to_move):
        """Takes a players name and a number between 1 and 6 as a parameter. The spaces to move will
        be added to the players current position.  If the property is owned by another player, rent will be
        deducted.  If the player does not have enough to pay the rent, the remaining account balance will
        be added to the property owners account balance.  The player's account balance will be zero and
        the property owner of their properties will be set to None
        """
        print(players_name, "has rolled a", spaces_to_move)
        self.set_player_current_position(players_name, spaces_to_move)
        new_current_space = self.get_player_current_position(players_name)
        owned_by = self._dictionary_of_spaces[new_current_space].get_owned_by()
        rent = self._dictionary_of_spaces[new_current_space].get_rent()
        property_name = self._dictionary_of_spaces[new_current_space].get_name()
        print(players_name, "has landed on", property_name)
        if self.get_player_account_balance(players_name) == 0:
            return

        if owned_by == players_name or owned_by == None:
            return
        else:
            rent_paid = self.pay_rent(players_name, rent)
            print(players_name, "paid", owned_by, ":", rent_paid)

            for player in self._player_list:
                if owned_by == player[0]:
                    player[2] += rent_paid
            self.get_player_current_position(players_name)

    def pay_rent(self, players_name, rent):
        """Helper method for move_player when a player lands on a property that is owned by someone else,
        and they have to pay rent"""
        for player in self._player_list:
            if players_name == player[0]:
                if player[2] >= rent:
                    player[2] -= rent
                    return rent

                if player[2] < rent:
                    money_left = player[2]
                    player[2] = 0
                    self.return_properties(players_name)
                    return money_left

    def return_properties(self, players_name):
        """Changes owner of properties to None when the owner's account balance is zero"""
        for key in self._dictionary_of_spaces:
            if key == 0:
                pass
            else:
                if self._dictionary_of_spaces[key].get_owned_by() == players_name:
                    self._dictionary_of_spaces[key].set_owned_by(None)

    def check_game_over(self):
        """Checks to see if all players but one have a zero account balance. If so, it returns the winners name.
        If there remains more than one player with a positive account balance, it returns a blank string"""
        game_check_list = self._player_list[:]

        for player in game_check_list:
            if player[2] == 0:
                game_check_list.remove(player)
        if len(game_check_list) > 1:
            return ""
        if len(game_check_list) == 1:
            winner = game_check_list[0][0]
            print("The winner is", winner)
            return winner


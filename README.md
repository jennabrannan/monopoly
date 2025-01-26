This program allows two or more players to play a simplified version of Monopoly called the
real estate game.  The properties are names of states in the US. The rents of the properties are passed in a list
as a parameter to the create_spaces method. Players are created through the create players method and given an initial
account balance as a parameter. All players start on "GO". On a players turn, the player is moved a number
of spaces that is passed as a parameter to move_player. Once the player lands on the property, if is not owned they
can purchase it at 5 times the rent value as long as they have an account balance greater than the purchase price.
If it is owned, the player must pay rent to the owner. When players pass go or land on go, they collect an amount
that is passed as a parameter to the create_spaces method.  Once a players account balance is 0 (any balance less than
zero is set to zero), the players properties are forfeited and now eligible to be purchased by other players. The game
is over when only 1 player has a balance greater than zero

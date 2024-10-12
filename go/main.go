package main

import (
	"fmt"
	"math/rand"
)

type Player struct {
	hand string
}

func (p Player) isWin(opponent Player) bool {
	if p.hand == "ぐー" && opponent.hand == "ちょき" {
		return true
	}
	if p.hand == "ちょき" && opponent.hand == "ぱー" {
		return true
	}
	if p.hand == "ぱー" && opponent.hand == "ぐー" {
		return true
	}
	return false
}

func getOppnentHand() string {
	var hands = [3]string{"ぐー", "ちょき", "ぱー"}
	return hands[rand.Intn(3)]
}

func isHandValid(inputHand string) bool {
	var hands = [3]string{"ぐー", "ちょき", "ぱー"}
	for _, hand := range hands {
		if hand == inputHand {
			return true
		}
	}
	return false
}

func main() {
	fmt.Print("じゃんけんしよう!")
	var userInput string
	fmt.Scan(&userInput)
	var userHand string
	if isHandValid(userInput) {
		userHand = userInput
	} else {
		fmt.Println("ぐー、ちょき、ぱーのいずれかを入力して下さい")
		return
	}
	user := &Player{
		hand: userHand,
	}
	opponent := &Player{getOppnentHand()}
	fmt.Println(opponent.hand)
	if user.isWin(*opponent) {
		fmt.Println("勝ち")
		return
	}
	if opponent.isWin(*user) {
		fmt.Println("負け")
		return
	}
	fmt.Println("引き分けです")
}

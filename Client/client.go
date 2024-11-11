package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os/user"
)

func main() {
	// Get current system user
	currentUser, err := user.Current()
	if err != nil {
		log.Fatal(err)
	}

	// Prepare the data to be sent
	data := map[string]string{
		"username": currentUser.Username,
	}

	// Convert data to JSON
	jsonData, err := json.Marshal(data)
	if err != nil {
		log.Fatal(err)
	}

	// Send the data to Django API
	resp, err := http.Post("http://127.0.0.1:8000/api/register/", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	// Print the response
	fmt.Println("Response status:", resp.Status)
}

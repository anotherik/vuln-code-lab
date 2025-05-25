package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"path/filepath"
)

const baseDir = "./files"

func viewHandler(w http.ResponseWriter, r *http.Request) {
	filename := r.URL.Query().Get("file")

	if filename == "" {
		http.Error(w, "Missing file parameter", http.StatusBadRequest)
		return
	}

	fullPath := filepath.Join(baseDir, filename)

	data, err := ioutil.ReadFile(fullPath)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error reading file: %v", err), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "text/plain")
	w.Write(data)
}

func main() {
	http.HandleFunc("/view", viewHandler)

	fmt.Println("Server running at http://localhost:8090/view?file=yourfile.txt")
	log.Fatal(http.ListenAndServe(":8090", nil))
}

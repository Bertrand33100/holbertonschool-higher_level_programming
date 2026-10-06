#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body to a CSV file."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                 for p in r.json()]
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts)

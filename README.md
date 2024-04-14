# Kioku
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

Kioku is a platform for people affected by dementia of any kind. Its goal is to slow the progression of memory loss. This goal is accomplished by playing simple memory based games, such as matching terms, flashcards, and simple puzzles. What's even better is that the platform is free and customizes to each person. A doctor, friend or family member can upload specific matching terms, flash cards, or puzzle images for practice. The best part of this is that you can set it up to specifically help your loved one remember you and their other family members.

## Technical Breakdown

Our tech stack for the frontend started with Sveltekit as the main main web framework. We used Tailwind and Flowbite to speed up styling and UI building. This tech stack on the frontend allowed us to develop much more quick;y providing us with many prebuilt components and provdiing us an easy to make our own components. Svelte forced us to have separation throughout our application as its routing is file structure based. This caused us t think deeply about what belongs on pages and what needs to be separated into components, and overall it provided us with a sturdy gaurd rail pushing us into good practices.

For the backend, we utilized Python's FastAPI library for it's speed of develop, efficiency while running, and overall code quality. This was a natural choice as it is a reliable backend that is quick and easy to write. Our database migration system and ORM of choice was Alembic and SQLAlchemy respectively. These packages became essential to the structure of our backend. Each logical section of the api gets its own router, each table gets a model from the ORM and a model for returning responses to requests. 

Holding everything together is Docker and Google Cloud. Docker made working across 3 different OSes not just possible but easy, and it even helped make our deployment easy as well. For deploying we utilized Google Cloud Platform (GCP). We have Continuous Deployment set up from our main branch such that any commit to Main is automatically built and deployed with zero down time. Cloud Run, the GCP product our runs on, also allows for scalability so our platform can handle a virtually limitless amount of people. Lastly for our production database and file storage, we are using Google Cloud SQL and Google Cloud Storage respectively due to the ease overall, but specifically the convenience of connecting Cloud Run.


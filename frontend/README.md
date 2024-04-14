# Project Title

## Non-Technical Introduction
- In a short summary, the goal of this project is to help slowen the brain deterioration that is caused by the Alzheimer's disease. The way this is done is by playing a series of matching, flashcard, and puzzle games featuring their friends and family that is uploaded by their loved ones.
- This is a problems that needs changing because there is very little options on the market, and the ones that exist are very expensive.

## Technical Breakdown
- Our tech-stack is mainly comprised of Sveltekit on the front end, fast API handling the backend, google cloud for our database/hosting.
- The way that the information is presented to the games is done by families uploading pictures into the main page which is then fed into the google cloud instance. This is then fetched by the svelte code and shown to the user in the various games.

## In-Depth Technical Sections
### Product deployment
- Purpose: Ensuring scalability of the project if needed to be accesed by a large audience
- In order to tackle the scalability of this project we decided to deploy on google cloud since it assures us that in case of a surge in users, it will be able to deliver a stable platform.

### Feature 1: Matching game
- Purpose: The propose of this game is in order to give the users of this game a way to remember their loved ones without having to feel the pressure of being quizzed or tested so they can learn (or relearn) about their family members stress free.
- One technical challenge that we ran into while making this minigame was making a way of telling when the two cards are overlapping, since sometimes a human can think they are overlapping the actual pixels might not. The way that we solved this problem was by making the "hitbox" of the cards bigger so when they are placed near each other they are classified as *overlapping*.

### Feature 2: Flashcard game
- Purpose: The overall propose of this game is very similar to the previous however there is one key difference in that the flashcards game involves more learning new content rather than getting quized on various memories. This can serve to be a more casual game (not that the matching game is not casual) in which the player can sit back and take in new information rather than trying to take a guess at first and then learning after the fact.

## Usage
- While the use case for this project might be very limited in target audience, it will make a great impact in the lives of those who are in need of such platform. This is because of expensive alternatives that are not very easily accessible for a product that could be implemented in such a simple fashion. 




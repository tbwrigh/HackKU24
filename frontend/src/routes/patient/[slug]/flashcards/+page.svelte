<script lang="ts">
  import type { Pair } from '$lib/types';
  import type { PageData } from './$types';
  import Flashcard from '$lib/flashcard.svelte';
  export let data: PageData;

  let currentIndex = 0;

  function nextFlashcard() {
    if (currentIndex < data.pairs.length - 1) {
      currentIndex++;
    }
  }

  function previousFlashcard() {
    if (currentIndex > 0) {
      currentIndex--;
    }
  }
</script>

<style>
  .flashcard-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    font-size: 6em; 
  }

  .flashcard {
    width: 40vw;
    height: 50vh;
    font-size: 5em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .next-button, .previous-button {
    position: fixed;
    bottom: 20px;
    font-size: 1em;
  }
.next-button {
  right: 50px;
  margin-bottom: 100px;
  height: 100px;
}

.previous-button {
  left: 50px;
  margin-bottom: 100px;
  height: 100px;
}
</style>

<div class="flashcard-container">
  <Flashcard pair={data.pairs[currentIndex]} />
  <button class="previous-button text-center font-medium focus-within:ring-4 focus-within:outline-none inline-flex items-center justify-center px-5 py-2.5 text-sm text-white bg-blue-700 hover:bg-blue-800 dark:bg-blue-600 dark:hover:bg-blue-700 focus-within:ring-blue-300 dark:focus-within:ring-blue-800 rounded-lg w-full1" on:click={previousFlashcard}>Previous</button>
  <button class="next-button text-center font-medium focus-within:ring-4 focus-within:outline-none inline-flex items-center justify-center px-5 py-2.5 text-sm text-white bg-blue-700 hover:bg-blue-800 dark:bg-blue-600 dark:hover:bg-blue-700 focus-within:ring-blue-300 dark:focus-within:ring-blue-800 rounded-lg w-full1" on:click={nextFlashcard}>Next</button>
</div>
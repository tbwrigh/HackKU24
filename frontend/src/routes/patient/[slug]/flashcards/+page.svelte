<script lang="ts">
  import type { PageData } from './$types';
  import { Button } from 'flowbite-svelte';
  import { ArrowLeftOutline, ArrowRightOutline } from 'flowbite-svelte-icons';
  import type { Pair } from '$lib/types';
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

<div class="flex flex-col justify-center items-center w-dvf h-dvh">
  <Flashcard pair={data.pairs[currentIndex]} />
  <navbar class="flex place-content-between">
    <Button on:click={previousFlashcard}>
      <ArrowLeftOutline class="w-8 h-8 text-gray-800" />
    </Button>
    <Button on:click={nextFlashcard}>
      <ArrowRightOutline class="w-8 h-8 text-gray-800" />
    </Button>
  </navbar>
</div>

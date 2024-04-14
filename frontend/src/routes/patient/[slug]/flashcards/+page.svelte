<script lang="ts">
  import type { PageData } from './$types';
  import type { Pair } from '$lib/types';
  import Flashcard from '$lib/flashcard.svelte';
  import ReturnModal from '$lib/returnModal.svelte';

  import { Button } from 'flowbite-svelte';
  import { ArrowLeftOutline, ArrowRightOutline } from 'flowbite-svelte-icons';

  export let data: PageData;

  let currentIndex = 0;
  let open: boolean = false;

  function nextFlashcard() {
    if (currentIndex < data.pairs.length - 1) {
      currentIndex++;
    }
    else {
      open = true;
    }
  }

  function previousFlashcard() {
    if (currentIndex > 0) {
      currentIndex--;
    }
  }
</script>

<div class="flex flex-col justify-center items-center w-dvf h-dvh">
  {#key currentIndex}
  <Flashcard pair={data.pairs[currentIndex]} />
  {/key}
  <navbar class="flex place-content-between">
    <Button on:click={previousFlashcard}>
      <ArrowLeftOutline class="w-8 h-8 text-gray-200" />
    </Button>
    <Button on:click={nextFlashcard}>
      <ArrowRightOutline class="w-8 h-8 text-gray-200" />
    </Button>
  </navbar>
</div>

<ReturnModal {open} route={"flashcards"} />

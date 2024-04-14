<script lang="ts">
  import type { Pair } from '$lib/types.ts';
  import { Card } from 'flowbite-svelte';
  import Element from '$lib/element.svelte';

  export let pair: Pair;

  let flipped: boolean = false;

</script>

<div class="flashcard-container p-4 min-w-[36rem] min-h-[20rem] max-w-[36rem] max-h-[20rem]">
  <Card on:click={() => flipped = !flipped} style={`perspective: 700px; text-align: center; transition: transform 0.3s; ${flipped ? "transform: rotateY(0.5turn)" : ""}`} class="w-full max-w-full h-full max-h-full justify-center">
    <div style="transform: rotateY(0.5turn)" class:hidden={!flipped}>
      <Element {pair} one_or_two={1} />
    </div>
    <div class:hidden={flipped}>
      <Element {pair} one_or_two={2} />
    </div>
  </Card>
</div>

<style>
  .flashcard-container {
    perspective: 1000px;
    transform-style: preserve-3d;
  }
</style>

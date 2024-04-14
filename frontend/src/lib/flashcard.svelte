<script lang="ts">
  import type { Pair } from '$lib/types.ts';
  import { Card } from 'flowbite-svelte';
  import Element from '$lib/element.svelte';

  export let pair: Pair;

  let flipped: boolean = false;

</script>

<div class="flashcard-container p-4">
  <Card on:click={() => flipped = !flipped} style={`perspective: 700px; text-align: center; transition: transform 0.3s; ${flipped ? "transform: rotateY(0.5turn)" : ""}`}>
    {#if flipped}
      <div style="transform: rotateY(0.5turn)">
        <Element {pair} one_or_two={1} />
      </div>
    {:else}
      <div>
        <Element {pair} one_or_two={2} />
      </div>
    {/if}
  </Card>
</div>

<style>
  .flashcard-container {
    perspective: 1000px;
    transform-style: preserve-3d;
  }
</style>

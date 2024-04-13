<script lang="ts">
  import { Card } from 'flowbite-svelte';

  let flipped: boolean = false;

</script>

<div class="flashcard-container p-4">
  <Card on:click={() => flipped = !flipped} style={`perspective: 700px; text-align: center; transition: transform 0.3s; ${flipped ? "transform: rotateY(0.5turn)" : ""}`}>
    {#if flipped}
      <div style="transform: rotateY(0.5turn)">
        <slot name="back" />
      </div>
    {:else}
      <div>
        <slot name="front" />
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

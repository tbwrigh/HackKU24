<script lang='ts'>
  import type { PageData } from './$types';
  import type { Pair } from '$lib/types';
  import Draggable from '$lib/draggable.svelte';

  export let data: PageData;

  let won: bool = false;

  let draggables = []

  function collisionCheck(thisdom, thispair) {
    if (won) return;
    draggables.forEach((otherDraggable) => {
      if (otherDraggable.dom === thisdom) return;
      const rect1 = thisdom.getBoundingClientRect();
      const rect2 = otherDraggable.dom.getBoundingClientRect();
      const buffer = 100;
      if (
        Math.abs(rect1.left - rect2.left) <= buffer &&
          Math.abs(rect1.top - rect2.top) <= buffer
      ) {
        thisdom.style.transition = 'opacity 1s';
        otherDraggable.dom.style.transition = 'opacity 1s';
        if (otherDraggable.pair.id == thispair.id) {
          thisdom.style.opacity = '0';
          otherDraggable.dom.style.opacity = '0';
          setTimeout(() => {
            thisdom.remove();
            otherDraggable.dom.remove();
            if (draggables.every((d) => d.dom === undefined || !d.dom.checkVisibility())) {
              won = true;
            }
          }, 1000);
        } else {
          thisdom.style.opacity = '1';
          otherDraggable.dom.style.opacity = '1';

          thisdom.style.backgroundColor = 'red';
          otherDraggable.dom.style.backgroundColor = 'red';
          setTimeout(() => {
            thisdom.style.backgroundColor = 'white';
            otherDraggable.dom.style.backgroundColor = 'white';
          }, 1000);
        }
      }
    });
  }

  // Finally this last bit of code is for running the entire element four times in order to get four individual
  // tiles. This number can change later down the road depending on how many tiles the player wants to play 
  // with.
</script>

{#each data.pairs as pair, i}
  <Draggable {pair} {collisionCheck} one_or_two={1} bind:this={draggables[2*i]} />
  <Draggable {pair} {collisionCheck} one_or_two={2} bind:this={draggables[2*i+1]} />
{:else}
  <p>No pairs detected for this patient</p>
{/each}

{#if won}
<div class="fixed w-dvw h-dvh flex justify-center place-content-center items-center">
  <p class="h-min text-4xl font-bold text-red-500">Congratulations, you got it!</p>
</div>
{/if}

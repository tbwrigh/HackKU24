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
      // can't collide with ourselves
      if (otherDraggable.dom === thisdom) return;

      const rect1 = thisdom.getBoundingClientRect();
      const rect2 = otherDraggable.dom.getBoundingClientRect();
      // if two rects are less than this distance apart, that counts as colliding
      const buffer = 100;

      if (
        Math.abs(rect1.left - rect2.left) <= buffer &&
        Math.abs(rect1.top - rect2.top) <= buffer
      ) {
        thisdom.style.transition = 'opacity 1s';
        otherDraggable.dom.style.transition = 'opacity 1s';

        // correct match
        if (otherDraggable.pair.id == thispair.id) {
          thisdom.style.opacity = '0';
          otherDraggable.dom.style.opacity = '0';
          setTimeout(() => {
            thisdom.remove();
            otherDraggable.dom.remove();
            // if for every draggable, its dom is undefined or has been removed
            if (draggables.every((d) => d.dom === undefined || !d.dom.checkVisibility())) {
              won = true;
            }
          }, 1000);
        }

        // incorrect match
        else {
          thisdom.style.opacity = '1';
          otherDraggable.dom.style.opacity = '1';
          thisdom.style.backgroundColor = 'red';
          otherDraggable.dom.style.backgroundColor = 'red';

          // revert white background color back to red after a delay
          setTimeout(() => {
            thisdom.style.backgroundColor = 'white';
            otherDraggable.dom.style.backgroundColor = 'white';
          }, 1000);
        }

      }
    });
  }

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

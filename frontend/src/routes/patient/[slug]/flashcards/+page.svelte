<script lang="ts">
  import type { Pair } from '$lib/types';
  import type { PageData } from './$types';
  import Flashcard from '$lib/flashcard.svelte';
  export let data: PageData;


  const pair: Pair = {
    id: 1,
    patient_id: 1,
    object_one_type: "string",
    object_one_value: "a",
    object_two_type: "string",
    object_two_value: "b",
  };

</script>

{#each data.pairs as pair, i}
  <Flashcard {pair} />
{/each}

<script lang="ts">
  import type { Pair } from '$lib/types';
  import Flashcard from '$lib/flashcard.svelte';

  const pair: Pair = {
    id: 1,
    patient_id: 1,
    object_one_type: "string",
    object_one_value: "a",
    object_two_type: "string",
    object_two_value: "b",
  };

</script>

  <p>Hello, can you see this?</p>
<Flashcard {pair} />

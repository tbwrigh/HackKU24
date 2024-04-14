<script lang="ts">
  import type { Pair } from '$lib/types';
  import Flashcard from '$lib/flashcard.svelte';

  const pair = Pair(1, 1, "string", "a", "string", "b");

</script>

<Flashcard {pair} />

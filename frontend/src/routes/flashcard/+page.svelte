<script lang="ts">
  import { ElementType } from '$lib/types.ts';
  import Element from '$lib/element.svelte';
  import Flashcard from '$lib/flashcard.svelte';

</script>

<Flashcard>
  <Element value={"front"} type={ElementType.Text} slot="front" />
  <Element value={"back"} type={ElementType.Text} slot="back" />
</Flashcard>

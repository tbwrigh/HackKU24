import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
  return {
    // placeholder values until we query the database
    slug: params.slug, // same as ID
    name: "John Doe",
  };
};

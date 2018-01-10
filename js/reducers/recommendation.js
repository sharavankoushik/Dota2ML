import hero_ids from '../hero_ids';

export default function recommendation(state = [], { type, payload }) {
  switch (type) {
    case 'RECOMMEND':
      const res = payload.data.map(id => {
        return hero_ids[`${id}`];
      });
      const prob = (payload.prob_x * 100).toFixed(2)
      const totalData = { data: res, prob };
      return totalData;
    default:
      return state;
  }
}

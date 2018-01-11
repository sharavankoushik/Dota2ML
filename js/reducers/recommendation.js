import hero_ids from '../hero_ids';

export default function recommendation(state = [], { type, payload }) {
  switch (type) {
    case 'RECOMMEND':
      const res = payload.data.map(id => {
        return hero_ids[`${id}`];
      });
      const indi_hero = payload.indi_hero.map(hero => { return (hero*100).toFixed(2)});
      console.log(indi_hero);
      const prob = (payload.prob_x * 100).toFixed(2)
      console.log(prob);
      const totalData = { data: res, prob, indi_hero };
      return totalData;
    default:
      return state;
  }
}

export default function enemy(state = [], action) {
  switch (action.type) {
    case 'ADD_ENEMY':
      const { payload } = action;
      return [...state, payload];
    default:
      return state;
  }
}

export default function hero(state = [], action) {
  switch (action.type) {
    case 'ADD_HERO':
      const { payload } = action;
      return [...state, payload];
    default:
      return state;
  }
}

export default function Heroes(state = {}, action) {
  const { payload } = action;
  let res = {};
  switch (action.type) {
    case 'HEROES':
      res = {
        type: 'LIST',
        payload
      };
      return { ...state, res };
    case 'REMOVE_HERO_FROM_LIST':
      res = {
        type: 'REMOVE',
        payload
      };
      return { ...state, res };
    case 'ADD_HERO_TO_LIST':
      res = {
        type: 'ADD',
        payload
      };
      return { ...state, res };
    default:
      return state;
  }
}

import { combineReducers } from 'redux';
import heros from './heros';
import hero from './hero';
import enemy from './enemy';
import recommendation from './recommendation';

const rootReducer = combineReducers({
  heros,
  hero,
  enemy,
  recommendation
});

export default rootReducer;

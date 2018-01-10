import heros from '../heros';
import axios from 'axios';

export const getHeroes = () => async dispatch => {
  dispatch({
    type: 'HEROES',
    payload: heros
  });
};

export const addHero = hero => async dispatch => {
  dispatch({
    type: 'ADD_HERO',
    payload: hero
  });
  dispatch({
    type: 'REMOVE_HERO_FROM_LIST',
    payload: hero
  });
};

export const addEnemy = hero => async dispatch => {
  dispatch({
    type: 'ADD_ENEMY',
    payload: hero
  });
  dispatch({
    type: 'REMOVE_HERO_FROM_LIST',
    payload: hero
  });
};

export const removeHero = hero => async dispatch => {
  dispatch({
    type: 'ADD_HERO_TO_LIST',
    payload: hero
  });
};

export const recommend = (heroList, enemyList) => async dispatch => {
  const x = heroList.map(hero => {
    return hero.id;
  });
  const y = enemyList.map(hero => {
    return hero.id;
  });
  const req = JSON.stringify({ x, y });
  const res = await axios.post('/api/recommend', req, {
    headers: { 'content-type': 'application/json' }
  });
  dispatch({
    type: 'RECOMMEND',
    payload: res.data
  });
};

import React, { Component } from 'react';
import {
  Grid,
  Container,
  Card,
  Image,
  Divider,
  Button
} from 'semantic-ui-react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { removeHero } from '../actions';

class Teams extends Component {
  constructor() {
    super();
    this.state = { heroes: [], enemies: [] };
    this.dummyHeroes = [
      {
        localized_name: 'hero1',
        id: 1,
        img:
          'https://orig00.deviantart.net/97fe/f/2013/332/c/4/dota_2_icon_by_benashvili-d6w0695.png'
      },
      {
        localized_name: 'hero2',
        id: 2,
        img:
          'https://orig00.deviantart.net/97fe/f/2013/332/c/4/dota_2_icon_by_benashvili-d6w0695.png'
      },
      {
        localized_name: 'hero3',
        id: 3,
        img:
          'https://orig00.deviantart.net/97fe/f/2013/332/c/4/dota_2_icon_by_benashvili-d6w0695.png'
      },
      {
        localized_name: 'hero4',
        id: 4,
        img:
          'https://orig00.deviantart.net/97fe/f/2013/332/c/4/dota_2_icon_by_benashvili-d6w0695.png'
      },
      {
        localized_name: 'hero5',
        id: 5,
        img:
          'https://orig00.deviantart.net/97fe/f/2013/332/c/4/dota_2_icon_by_benashvili-d6w0695.png'
      }
    ];
  }

  componentWillReceiveProps(props) {
    const { heroes, enemies } = props;
    this.setState({ heroes, enemies });
    if (heroes.length > 0) {
      this.setState({ availability: true });
    }
  }

  removehero = (e, { hero, type }) => {
    if (type === 'hero') {
      const { heroes } = this.state;
      var removeIndex = heroes
        .map(function(item) {
          return item.id;
        })
        .indexOf(hero.id);
      heroes.splice(removeIndex, 1);
      this.setState({ heroes });
    }
    if (type === 'enemy') {
      const { enemies } = this.state;
      var removeIndex = enemies
        .map(function(item) {
          return item.id;
        })
        .indexOf(hero.id);
      enemies.splice(removeIndex, 1);
      this.setState({ enemies });
    }
    this.props.removeHero(hero);
  };

  renderHeroes(list, type) {
    let renderedList = null;
    let availability = null;
    if (list.length === 0) {
      renderedList = this.dummyHeroes;
      availability = false;
    } else {
      renderedList = list;
      availability = true;
    }
    return renderedList.map(hero => {
      return (
        <Grid.Column key={hero.id}>
          <Card>
            <Image src={hero.img} size="medium" />
            <Card.Header
              as="h3"
              textAlign="center"
              style={{ textTransform: 'capitalize' }}
            >
              {hero.localized_name}
            </Card.Header>
            {availability ? (
              <Card.Content extra>
                <Button
                  basic
                  color="red"
                  hero={hero}
                  onClick={this.removehero}
                  type={type}
                >
                  Remove
                </Button>
              </Card.Content>
            ) : null}
          </Card>
        </Grid.Column>
      );
    });
  }

  render() {
    const { heroes, enemies } = this.state;
    return (
      <Container fluid style={{ overflowY: 'hidden', overflowX: 'hidden' }}>
        <Grid centered stackable columns={5}>
          <Grid.Row>
            <Divider horizontal>Our Team</Divider>
            {this.renderHeroes(heroes, 'hero')}
          </Grid.Row>
          <Grid.Row>
            <Divider horizontal>Their Team</Divider>
            {this.renderHeroes(enemies, 'enemy')}
          </Grid.Row>
        </Grid>
      </Container>
    );
  }
}
function mapStateToProps({ hero, enemy }) {
  return {
    heroes: hero,
    enemies: enemy
  };
}

function mapStateToDispatch(dispatch) {
  return bindActionCreators({ removeHero }, dispatch);
}

export default connect(mapStateToProps, mapStateToDispatch)(Teams);

/**
 *


 <Divider horizontal>Their Team</Divider>
 {this.state.enemies.map(hero => {
   return (
     <Grid.Column key={hero.id}>
       <Card>
         <Image src={hero.img} size="medium" />
         <Card.Header>{hero.localized_name}</Card.Header>
       </Card>
     </Grid.Column>
   );
 })}
 */

import React, { Component } from 'react';
import {
  Container,
  Sidebar,
  Card,
  Button,
  Image,
  Grid
} from 'semantic-ui-react';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { getHeroes, addHero, addEnemy } from '../actions';

class Heroes extends Component {
  state = {
    heros: [],
    heroAvail: true,
    enemyAvail: true,
    availability: true
  };
  componentWillReceiveProps(props) {
    if (props.heros.type === 'LIST') {
      this.setState({ heros: props.heros.payload });
    } else if (props.heros.type === 'ADD') {
      const { heros } = this.state;
      heros.push(props.heros.payload);
      this.setState({ heros });
    } else {
      const { heros } = this.state;
      var removeIndex = heros
        .map(function(item) {
          return item.id;
        })
        .indexOf(props.heros.payload.id);
      heros.splice(removeIndex, 1);
      this.setState({ heros });
    }
    if (props.hero.length === 5) {
      this.setState({ heroAvail: false });
    }else
    {
      this.setState({ heroAvail: true });
    }
    if (props.enemy.length === 5) {
      this.setState({ enemyAvail: false });
    }else{
      this.setState({ enemyAvail: true });
    }
    if (!(this.state.heroAvail && this.state.enemyAvail)) {
      this.setState({ availability: false });
    }
  }

  componentDidMount() {
    this.props.getHeroes();
  }

  handleHero = (event, { data }) => {
    this.props.addHero(data);
  };

  handleEnemy = (event, { data }) => {
    this.props.addEnemy(data);
  };

  render() {
    return (
      <Container
        style={{
          overflowY: 'scroll',
          maxHeight: '90vh',
          padding: 10
        }}
      >
        <Grid columns={2} centered>
          {this.state.heros.map(hero => {
            return (
              <Grid.Column key={hero.id}>
                <Card>
                  {this.state.heroAvail ? (
                    <Card.Content extra>

                        <Button
                          basic
                          color="green"
                          onClick={this.handleHero}
                          data={hero}
                        >
                          Hero
                        </Button>

                    </Card.Content>
                  ): null}
                  <Image size="medium" src={hero.img} />
                  <Card.Header as="h3" textAlign="center">
                    {hero.localized_name}
                  </Card.Header>

                  {this.state.enemyAvail ?  (
                    <Card.Content extra>
                        <Button
                          basic
                          color="red"
                          onClick={this.handleEnemy}
                          data={hero}
                        >
                          Enemy
                        </Button>
                    </Card.Content>
                  ):null }
                </Card>
              </Grid.Column>
            );
          })}
        </Grid>
      </Container>
    );
  }
}

function mapStateToProps({ heros: { res }, hero, enemy }) {
  return {
    heros: res,
    hero,
    enemy
  };
}

function mapStateToDispatch(dispatch) {
  return bindActionCreators({ getHeroes, addHero, addEnemy }, dispatch);
}

export default connect(mapStateToProps, mapStateToDispatch)(Heroes);

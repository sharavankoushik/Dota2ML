import React, { Component } from 'react';
import {
  Container,
  Grid,
  Card,
  Image,
  Button,
  Divider,
  Statistic
} from 'semantic-ui-react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import Teams from './teams';
import { recommend, addHero } from '../actions';

class Recommender extends Component {
  state = {loading:false};
  recommender = () => {
    this.props.recommend(this.state.heroes, this.state.enemies);
    this.setState({loading : true})
  };
  componentWillReceiveProps({ hero, enemy, recommendation, prob }) {
    this.setState({
      heroes: hero,
      enemies: enemy,
      recommendation,
      prob,
      loading : false
    });
  }

  removehero = hero => {
    const { recommendation } = this.state;
    var removeIndex = recommendation
      .map(function(item) {
        return item.id;
      })
      .indexOf(hero.id);
    recommendation.splice(removeIndex, 1);
    this.setState({ recommendation });
  };

  handleAdd = (e, { hero }) => {
    this.props.addHero(hero);
    this.removehero(hero);
  };

  renderRecommendation() {
    return this.props.recommendation.map(hero => {
      return (
        <Grid.Column key={hero.id}>
          <Card>
            <Image src={hero.img} size="medium" />
            <Card.Header as="h3" textAlign="center">
              {hero.localized_name}
            </Card.Header>
            <Card.Content extra>
              <Button basic color="green" onClick={this.handleAdd} hero={hero}>
                Add to my list
              </Button>
            </Card.Content>
          </Card>
        </Grid.Column>
      );
    });
  }

  render() {
    let bool = this.state.recommendation;
    if (bool) {
      bool = this.state.recommendation.length > 0;
    }
    return (
      <Grid centered stackable stretched>
        <Grid.Row>
          <Teams />
        </Grid.Row>
        <Grid.Row>
          {bool ? (
            <Container fluid>
              <Divider horizontal>Recommended Heroes</Divider>
              <Statistic>
                <Statistic.Value>{this.state.prob}%</Statistic.Value>
                <Statistic.Label>The probability of picks winning based on the opponenets chosen</Statistic.Label>
              </Statistic>
              <Grid columns={5} centered stretched>
                {this.renderRecommendation()}
              </Grid>
            </Container>
          ) : null}
        </Grid.Row>
        <Grid.Row>
          {this.props.show ? (
            <Button basic color="blue" onClick={this.recommender} loading = {this.state.loading}>
              Recommend
            </Button>
          ) : null}
        </Grid.Row>
      </Grid>
    );
  }
}

function mapStateToProps({ enemy, hero, recommendation: { prob, data } }) {
  let show = false;
  if (enemy.length > 0) {
    show = true;
  }
  return { show, enemy, hero, recommendation: data, prob };
}

function mapStateToDispatch(dispatch) {
  return bindActionCreators({ recommend, addHero }, dispatch);
}

export default connect(mapStateToProps, mapStateToDispatch)(Recommender);

import React, {Component} from 'react';
import {Button, Card, Container, Divider, Grid, Image, Statistic} from 'semantic-ui-react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import Teams from './teams';
import {addHero, recommend} from '../actions';

class Recommender extends Component {
    state = {loading: false};
    recommender = () => {
        this.props.recommend(this.state.heroes, this.state.enemies);
        this.setState({loading: true})
    };
    removehero = hero => {
        const {recommendation} = this.state;
        var removeIndex = recommendation
            .map(function (item) {
                return item.id;
            })
            .indexOf(hero.id);
        recommendation.splice(removeIndex, 1);
        this.setState({recommendation});
    };
    handleAdd = (e, {hero}) => {
        this.props.addHero(hero);
        this.removehero(hero);
    };

    componentWillReceiveProps({hero, enemy, recommendation, prob, prob_every_hero}) {
        this.setState({
            heroes: hero,
            enemies: enemy,
            recommendation,
            prob,
            prob_every_hero,
            loading: false
        });
    }

    renderRecommendation() {
        return this.props.recommendation.map(hero => {
            return (
                <Grid.Column key={hero.id}>
                    <Card>
                        <Image src={hero.img} size="large"/>
                        <Card.Header as="h3" textAlign="center">
                            {hero.localized_name}
                        </Card.Header>
                        <Statistic><Statistic.Label>Percentage of each Hero</Statistic.Label>
                            {
                                this.state.prob_every_hero.map(prob => {
                                    return (<Statistic.Value key={prob}>{prob}%</Statistic.Value>)
                                })
                            }
                        </Statistic>
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

    /*main render function*/
    render() {
        let bool = this.state.recommendation;
        console.log(bool);
        if (bool) {
            bool = this.state.recommendation.length > 0;
        }
        return (
            <Grid centered stackable stretched>
                <Grid.Row>
                    <Teams/>
                </Grid.Row>
                <Grid.Row>
                    {bool ? (
                        <Container fluid>
                            <Divider horizontal>Recommended Heroes</Divider>
                            <Statistic>
                                <Statistic.Value>{this.state.prob}%</Statistic.Value>
                                <Statistic.Label>The probability of picks winning based on the opponenets
                                    chosen</Statistic.Label>
                            </Statistic>
                            <Grid columns={5} centered stretched>
                                {this.renderRecommendation()}
                            </Grid>
                        </Container>
                    ) : null}
                </Grid.Row>
                <Grid.Row>
                    {this.props.show ? (
                        <Button basic color="blue" onClick={this.recommender} loading={this.state.loading}>
                            Recommend
                        </Button>
                    ) : null}
                </Grid.Row>
            </Grid>
        );
    }
}

function mapStateToProps({enemy, hero, recommendation: {prob, data, indi_hero}}) {
    let show = false;
    if (enemy.length > 0) {
        show = true;
    }
    return {show, enemy, hero, recommendation: data, prob, prob_every_hero: indi_hero};
}

function mapStateToDispatch(dispatch) {
    return bindActionCreators({recommend, addHero}, dispatch);
}

export default connect(mapStateToProps, mapStateToDispatch)(Recommender);

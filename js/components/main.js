import React, { Component } from 'react';
import { Grid, Container, Segment, Rail } from 'semantic-ui-react';
import Heroes from './heroes';
import Recommender from './recommender';

export default class Main extends Component {
  render() {
    return (
      <Grid columns={2} centered stretched>
        <Grid.Column>
          <Segment style={{ width: '70vw' }}>
            <Recommender />
            <Rail attached position="left">
              <Heroes />
            </Rail>
          </Segment>
        </Grid.Column>
      </Grid>
    );
  }
}

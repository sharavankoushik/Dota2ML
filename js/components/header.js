import React, { Component } from 'react';
import { Container, Header } from 'semantic-ui-react';

export default class NavBar extends Component {
  render() {
    return (
      <Container style={{ marginTop: 15 }}>
        <Header as="h1">Dota Recommendation Engine</Header>
      </Container>
    );
  }
}

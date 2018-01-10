import React, { Component } from 'react';
import { Container } from 'semantic-ui-react';
import NavBar from './components/header';
import Main from './components/main';

export default class App extends Component {
  render() {
    return (
      <Container fluid>
        <NavBar />
        <Main />
      </Container>
    );
  }
}

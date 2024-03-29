import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QuestaoLista from "./QuestaoLista";
import axios from "axios"; //(12)
import { API_URL_QUESTOES, API_URL_OPCOES } from "../constants";
//(13)
class Home extends Component { //(14)
    state = { //(15)
        questoes: [],
        opcoes: []
    };
    componentDidMount() { //(16)
        this.resetState();
    }
    getQuestoes = () => {
        axios.get(API_URL_QUESTOES).then(res => this.setState({
            questoes:
                res.data
        })); //(17)
    };
    getOpcoes = () => {
        axios.get(API_URL_OPCOES).then(res => this.setState({
            opcoes:
                res.data
        })); //(18)
    };
    resetState = () => { //(16)
        this.getQuestoes();
        this.getOpcoes();
    };
    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                        <QuestaoLista
                            questoes={this.state.questoes}
                            opcoes={this.state.opcoes}
                            resetState={this.resetState}
                        />
                    </Col>
                    16
                </Row>
            </Container>
        );
    }
}
export default Home;
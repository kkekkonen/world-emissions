import React, { Component } from "react";
import ReactChartkick, { LineChart } from 'react-chartkick'
import Chart from 'chart.js'

ReactChartkick.addAdapter(Chart)

export default class EmissionChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mode: "",
            countryData: [],
            topEmissions: [],
            nations: [],
            nation: {},
			nationToCompare: {},
            perCapita: false
        };
    }

    setPerCapita = (event) => {
        //this function is called when the per capita tickbox is selected
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        this.processNation(this.state.nation.name, value)
    }

    findArrayElement = (element, name) => {
        return name === element.name
    }

    selectNation = (event) => {
        //this function is called when the nation is changes on single nation graph
        this.processNation(event.target.value, this.state.perCapita)
    }

	selectPrimaryNation = (event) => {
        //this function is called when the user selects the first country to compare agains the second
		const nation = this.state.countryData.find(country => country.name === event.target.value)
		this.setState({nation})
	}

	selectNationToCompare = (event) => {
        //this function is called when the second country is selected to compare against the first
		const nationToCompare = this.state.countryData.find(country => country.name === event.target.value)
		this.setState({nationToCompare})
	}

    processNation = (countryName, perCapita) => {
        //this function creates the graph used in single country graph. Some computation is needed if the per capita tickbox is selected
        const nation = this.state.countryData.find(country => country.name === countryName)
        let emission_values = {}
        if (perCapita && nation) {
            try{
                fetch('/country_population/' + nation.Country_Code)
                    .then(response => response.json())
                    .then(data => Object.keys(data.data).map(year =>
                        {if(nation.data[year] && data.data[year]) {
                            emission_values[year] = nation.data[year] /  data.data[year]
                        }}
                    ))
                    .then( () => this.setState({nation: { ...nation, ...{ data: emission_values } }, perCapita}))
            } catch {
                this.setState({nation, perCapita})
            }
        }
        this.setState({nation, perCapita})
    }

    changeMode = (event) => {
        //this function changes the mode of the visualization
        this.setState({mode: event.target.value, nation: {}, nationToCompare: {}})
    }

    processData = (data) => {
        //this function processes the data previously fetched when the component loads
        let nations = [];
        let topEmissions = [];
        data.forEach(function (value, index){
            nations.push(value.name)
            const current_emissions = value.data[(new Date()).getFullYear() - 5]
            if (current_emissions){
                if (topEmissions.length < 10) {
                    topEmissions.push({name: value.name, data: value.data, emissions: value.data[(new Date()).getFullYear() - 5]})
                } else {
                    const topEmissionsMinimum = topEmissions.reduce((min, p) => p.emissions < min.emissions ? p : min, topEmissions[0])
                    if (current_emissions > topEmissionsMinimum.emissions) {
                        topEmissions.splice(topEmissions.indexOf(topEmissionsMinimum), 1);
                        topEmissions.push({name: value.name, data: value.data, emissions: value.data[(new Date()).getFullYear() - 5]})
                    }
                };
            };
        });
        this.setState({countryData: data, topEmissions, nations})
    }

    componentDidMount() {
        //when the component mounts, the country json file is fetched and processed
        try{
            fetch('/emission_json')
                .then(response=> response.json())
                .then(data => this.processData(data))
        } catch (error){
            console.warn(error);
        }
    }

    render() {
        return (
            <div className="App">
                <select onChange={this.changeMode}>
                    <option value={''}> select mode </option>
                    <option value={'nation'}>nation</option>
					<option value={'compare nations'}>compare nations</option>
                    <option value={'top emissions'}>top emissions</option>
                </select>
                {this.state.mode === 'nation' &&
                    <div>
                        <select onChange={this.selectNation}>
                            <option value={""}>select nation</option>
                            {this.state.nations.map((nation, i) => <option value={nation} key={i}>{nation}</option>)}}
                        </select>
						<label>Show per capita</label>
                        <input
                          name="perCapita"
                          type="checkbox"
                          checked={this.state.perCapita}
                          onChange={this.setPerCapita} />
                    </div>
                }
				{this.state.mode === 'compare nations' &&
                    <div>
                        <select onChange={this.selectPrimaryNation}>
                            <option value={""}>select nation 1</option>
                            {this.state.nations.map((nation, i) => <option value={nation} key={i}>{nation}</option>)}}
                        </select>
						<select onChange={this.selectNationToCompare}>
                            <option value={""}>select nation 2</option>
                            {this.state.nations.map((nation, i) => <option value={nation} key={i + "#compare"}>{nation}</option>)}}
                        </select>
                    </div>
                }
                {this.state.mode === 'top emissions' &&
                    <LineChart data={this.state.topEmissions} />
                }
                {this.state.mode === 'nation' && Object.keys(this.state.nation).length !== 0 &&
                    <LineChart data={this.state.nation.data} />
                }
				{this.state.mode === 'compare nations' && Object.keys(this.state.nation).length !== 0 && Object.keys(this.state.nationToCompare).length !== 0 &&
                    <LineChart data={[this.state.nation, this.state.nationToCompare]} />
                }
            </div>
        );
    }
}

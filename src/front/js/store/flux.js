const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			user: [],
			token: [],
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},
			logIn: async (email, password, navigate) => {
				setStore({ loading: true })
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/login`, {
						method: POST,
						headers: {
							"content-type": "application/json"
						},
						body: JSON.stringify({ email, password })
					})
					if (response.ok) {
						const data = await response.json();
						setStore({ token: data.token, user: data.user, loading: false });
						localStorage.setItem("token", data.token)
						console.log("User successfully logged in.");
						navigate("/");
					} else {
						const errorData = await response.json();
						alert(errorData.message || "Invalid credentials. Please try again.");
						setStore({ loading: false });
					}
				}
				catch (error) {
					console.error("Error in logIn:", error);
					alert("An error occurred during login. Please try again later.");
					setStore({ loading: false });
				}
			},
			signUp: async (name, email, password, navigate) => {
				setStore({ loading: true })
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/signup`, {
						method: POST,
						headers: {
							"content-type": "application/json"
						},
						body: JSON.stringify({ name, email, password })
					})
					if (response.ok) {
						console.log("signup succesfully");
					} else {
						const errorData = await response.json(); // Captura detalles del error
						console.log("Failed to register user:", errorData);
						alert(errorData.message || "Registration failed. Please try again.");
					}
				}
				catch (error) {
					console.error("Error in signUp:", error);
					alert("An error occurred during registration. Please try again later.");
				} finally {
					setStore({ loading: false }); // Finaliza el estado de carga
				}
			},
			addPerson: async (name, race, height) => {
				setStore({ loading: true })
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/addperson`, {
						method: POST,
						headers: {
							"content-type": "application/json"
						},
						body: JSON.stringify({ name, race, height })
					})
					if (response.ok) {
						console.log("person added succesfully");
					} else {
						const errorData = await response.json(); // Captura detalles del error
						console.log("Failed to add person:", errorData);
						alert(errorData.message || "adding failed. Please try again.");
					}
				}
				catch (error) {
					console.error("Error in adding:", error);
					alert("An error occurred during adding. Please try again later.");
				} finally {
					setStore({ loading: false }); // Finaliza el estado de carga
				}
			},
			addWeapon: async (name, type, built) => {
				setStore({ loading: true })
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/addweapon`, {
						method: POST,
						headers: {
							"content-type": "application/json"
						},
						body: JSON.stringify({ name, type, built })
					})
					if (response.ok) {
						console.log("weapon added succesfully");

					} else {
						const errorData = await response.json(); // Captura detalles del error
						console.log("Failed to add weapon:", errorData);
						alert(errorData.message || "adding failed. Please try again.");
					}
				}
				catch (error) {
					console.error("Error in adding:", error);
					alert("An error occurred during adding. Please try again later.");
				} finally {
					setStore({ loading: false }); // Finaliza el estado de carga
				}
			},
			addPlace: async (name, location, population) => {
				setStore({ loading: true })
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/addplace`, {
						method: POST,
						headers: {
							"content-type": "application/json"
						},
						body: JSON.stringify({ name, location, population })
					})
					if (response.ok) {
						console.log("place added succesfully");
					} else {
						const errorData = await response.json(); // Captura detalles del error
						console.log("Failed to add place:", errorData);
						alert(errorData.message || "adding failed. Please try again.");
					}
				}
				catch (error) {
					console.error("Error in adding:", error);
					alert("An error occurred during adding. Please try again later.");
				} finally {
					setStore({ loading: false }); // Finaliza el estado de carga
				}

			},

			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
// logIn: async (email,password,navigate) => {
// 	setStore({loading: true})
// 	try{
// 		const response = await fetch(`${process.env.BACKEND_URL}/api/login`,{
// 			method: POST,
// 			headers: {
// 				"content-type": "application/json"
// 			},
// 			body: JSON.stringify({email,password})
// 		})
// 		if (response.ok) {
// 			const data = await response.json();
// 			setStore({ token: data.token, user: data.user, loading: false }); 
// 			localStorage.setItem("token", data.token)
// 			console.log("User successfully logged in.");
// 			navigate("/"); 
// 		} else {
// 			const errorData = await response.json(); 
// 			alert(errorData.message || "Invalid credentials. Please try again.");
// 			setStore({ loading: false });
// 		}
// 	}
// 	catch (error) {
// 		console.error("Error in logIn:", error);
// 		alert("An error occurred during login. Please try again later.");
// 		setStore({ loading: false });
// 	} 
// },
// signUp: async (name,email,password,navigate) => {
// 	setStore({loading: true})
// 	try{
// 		const response = await fetch(`${process.env.BACKEND_URL}/api/signup`, {
// 			method: POST,
// 			headers: {
// 				"content-type": "application/json"
// 			},
// 			body: JSON.stringify({name,email,password})
// 		})
// 		if(response.ok){
// 			console.log("logged in succesfully");
// 		}
// 		else {
// 			const errorData = await response.json(); // Captura detalles del error
// 			console.log("Failed to register user:", errorData);
// 			alert(errorData.message || "Registration failed. Please try again.");
// 		}
// 	}
// 	catch (error) {
// 		console.error("Error in signUp:", error);
// 		alert("An error occurred during registration. Please try again later.");
// 	} finally {
// 		setStore({ loading: false }); // Finaliza el estado de carga
// 	}
// },
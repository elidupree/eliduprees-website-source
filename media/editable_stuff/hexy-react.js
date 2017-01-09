(function(){
  "use strict"
  
  function get_link (whatever) {return whatever.getAttributeNS('http://www.w3.org/1999/xlink', 'href'); }
  function set_link (whatever, value) {return whatever.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value); }
  
  function iterate_sources (element, callback) {
    callback (element);
    var link = get_link (element);
    if (link) {iterate_sources (document.getElementById (link.slice (1)), callback);}
    $(element).children().each (function() {iterate_sources (this, callback);});
  }
  
  function random_range (min, max) {
    return min + Math.floor (Math.random()*(max - min));
  }
  function random_choice (sequence) {
    return sequence [random_range (0, sequence.length)];
  }

  var tile_ids = window.hexy_tile_ids
  var blank_hex_id = "g7168"
  var long_radius = 36;
  var short_radius = long_radius*0.866;
   function tile_position (horizontal, vertical) {
    if (vertical === undefined) {vertical = horizontal.vertical; horizontal = horizontal.horizontal;}
    return {horizontal: horizontal*1.5*long_radius, vertical: vertical*short_radius}
  }
  
  // CSS rotations are clockwise, so I'm making the directions be clockwise so that I don't screw up.
  // Direction 0 is up in user space, up-right in the source (I rotate the tiles by 1/2
  // because I'm familiar with hexagonal tiles being oriented that way in Wesnoth)
  var directions = [
    {horizontal:  0, vertical: -2},
    {horizontal:  1, vertical: -1},
    {horizontal:  1, vertical:  1},
    {horizontal:  0, vertical:  2},
    {horizontal: -1, vertical:  1},
    {horizontal: -1, vertical: -1}
  ];
  
  function in_direction (location, direction) {
    var offset = directions [direction];
    return {horizontal: location.horizontal + offset.horizontal, vertical: location.vertical + offset.vertical};
  }
  
  function position_string (location) {
    return location.horizontal.toString() + "_" + location.vertical;
  }
  
  var dead= "dead";var icon= "icon";var lock= "lock";
  var connections_table = {
    [blank_hex_id]: { offset: {horizontal: 0, vertical: 1050.862}},
  
    g8043: {connections: [3, 2, 1, 0, 5, 4], offset: {horizontal: 3, vertical: 1038.862}, weight: 10, pieces: ["use7975","use8039","use8041"]},
    g8261: {connections: [2, 4, 0, 5, 1, 3], offset: {horizontal: 3, vertical: 1026.862}, weight: 15, pieces: ["use8257","use8259","use8255"]},
    g8571: {connections: [2, 3, 0, 1, 5, 4], offset: {horizontal: 3, vertical: 1014.862}, weight: 15, pieces: ["use8567","use8565","use8569"]},
    g8657: {connections: [1, 0, 3, 2, 5, 4], offset: {horizontal: 20, vertical: 1007.862}, weight: 4, pieces: ["use8655","use8653","use8651"]},
    g8985: {connections: [3, 4, 5, 0, 1, 2], offset: {horizontal: 20, vertical: 1001.862}, weight: 0, pieces: ["use8983","use8981","use8979"]},
    
    
    g9384: {connections: [5, dead, icon, 4, 3, 0], offset: {horizontal: 20, vertical: 1036.862}, weight: 8, pieces: ["use9344","use9348","use9382","use9346"]},
    g9425: {connections: [1, 0, icon, 4, 3, dead], offset: {horizontal: 20, vertical: 1036.862 - 2}, weight: 34, pieces: ["use9395","use9401","use9397","use9399"]},
    g9432: {connections: [1, 0, icon, dead, 5, 4], offset: {horizontal: 20, vertical: 1036.862 - 4}, weight: 8, pieces: ["use9409","use9413","use9411","use9407"]},
    g9631: {connections: [2, 3, 0, 1, icon, dead], offset: {horizontal: 20, vertical: 1036.862-6}, weight: 29, pieces: ["g9154","g9144","use9607","use9609"]},
    g9625: {connections: [2, 3, 0, 1, dead, icon], offset: {horizontal: 20, vertical: 1036.862-8}, weight: 29, pieces: ["g9154","g9144","use9617","use9615"]},
    g9812: {connections: [4, 2, 1, icon, 0, dead], offset: {horizontal: 20, vertical: 1036.862-10}, weight: 10, pieces: ["use9798","use9796","use9800","use9794"]},
    g9843: {connections: [2, dead, 0, icon, 5, 4], offset: {horizontal: 20, vertical: 1036.862-12}, weight: 10, pieces: ["use9806","use9810","use9808","use9804"]},
    g10007: {connections: [3, 2, 1, 0, icon, dead], offset: {horizontal: 20, vertical: 1036.862-14}, weight: 24, pieces: ["use9987","use9995","use9993","use9991"]},
    g10014: {connections: [3, 2, 1, 0, dead, icon], offset: {horizontal: 20, vertical: 1036.862-16}, weight: 24, pieces: ["use10001","use9999","use10003","use10005"]},
    g10195: {connections: [3, 4, dead, 0, 1, icon], offset: {horizontal: 20, vertical: 1036.862-18}, weight: 0},
    g10315: {connections: [2, 4, 0, dead, 1, icon], offset: {horizontal: 20, vertical: 1036.862-20}, weight: 0},
    g10325: {connections: [icon, 4, dead, 5, 1, 3], offset: {horizontal: 20, vertical: 1036.862-22}, weight: 0},
    g10573: {connections: [lock, lock, lock, 5, lock, 3], offset: {horizontal: 20, vertical: 1012.862}, weight: 1},
    g10495: {connections: [2, 3, 0, 1, lock, lock], offset: {horizontal: 20, vertical: 1010.862}, weight: 3},
  };
  document.getElementById ("use10453").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use15461").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10515").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10539").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("path15465").style.setProperty ("--path-fill", "var(--path-fill-lock)");
  document.getElementById ("use10527").style.setProperty ("--path-fill", "var(--path-fill-3-5)");
  
  var icons_table = {
    g9171: {grid_position: 1, icon: "hand", color: "black", side: "right", weight: 12},
    g9179: {grid_position: 2, icon: "hand", color: "white", side: "right", weight: 12},
    g9187: {grid_position: 3, icon: "hand", color: "black", side: "left", weight: 12},
    g9202: {grid_position: 4, icon: "hand", color: "white", side: "left", weight: 12},
    g9224: {grid_position: 5, icon: "foot", color: "black", side: "right", weight: 6},
    g9231: {grid_position: 6, icon: "foot", color: "white", side: "right", weight: 6},
    g9217: {grid_position: 7, icon: "foot", color: "black", side: "left", weight: 6},
    g9210: {grid_position: 8, icon: "foot", color: "white", side: "left", weight: 6},
    g9278: {grid_position: 11, icon: "crotch", color: "black", weight: 17},
    g9267: {grid_position: 12, icon: "crotch", color: "white", weight: 17},
    g9289: {grid_position: 9, icon: "torso", color: "black", weight: 23},
    g9299: {grid_position: 10, icon: "torso", color: "white", weight: 23},
    g9250: {grid_position: 13, icon: "furniture", weight: 16},
    g9238: {grid_position: 14, icon: "toybox", weight: 8},
  };
   
  Object.getOwnPropertyNames(connections_table).forEach(function(id) {
    var info = connections_table [id];
    info .id = id;
    info.offset.horizontal += 0.866;
    info.offset.vertical += 1;
    var piece_index = 0;
    if (info.connections) {info.connections.forEach(function(connection, index) {
      function do_connection (identifier) {
        if (!info.pieces) {return;}
        //console.log (info.pieces [piece_index]);
        var piece_element = document.getElementById (info.pieces [piece_index]);
        piece_element.style.setProperty ("--path-fill", "var(--path-fill-" + identifier +")");
        //piece_element.style.setProperty ("transition-delay", "1s");
        ++piece_index;
      }
      if (typeof connection == "number") {
        if (info.connections[connection] !== index) {
          console.log ("error: mismatched connections");
        }
        if (index <connection) {
          do_connection (index + "-" + connection);
        }
      }
      else if (connection == "lock") {
        do_connection ("lock");
      } else {
        do_connection (index + "-" + connection);
      }
    });}
    iterate_sources (document.getElementById (id), function(source) {
      //if (source.style.fill) {source.style.setProperty ("transition-delay", "1s"); }
      source.style.removeProperty ("filter");
    });
  });
  
  Object.getOwnPropertyNames(icons_table).forEach(function(id) {
    var info = icons_table [id];
    info .id = id;
    iterate_sources (document.getElementById (id), function(source) {
      if (info . color === "black") {
        if (source.style.fill === "rgb(0, 0, 0)") {source.style.fill = "var(--icon-fill)";}
        if (source.style.stroke === "rgb(255, 255, 255)") {source.style.stroke = "var(--icon-stroke)";}
        if (source.style.fill === "rgb(255, 255, 255)") {source.style.fill = "var(--icon-stroke)";}
      }
      if (info . color === "white") {
        if (source.style.fill === "rgb(255, 255, 255)") {source.style.fill = "var(--icon-fill)";}
        if (source.style.stroke === "rgb(0, 0, 0)") {source.style.stroke = "var(--icon-stroke)";}
        if (source.style.fill === "rgb(0, 0, 0)") {source.style.fill = "var(--icon-stroke)";}
      }
    });
  });
  
  
  function get_tile_info (element) {
    var original = (typeof element === "string") && ('#'+element) || get_link (element);
    var direct = connections_table [original.slice (1)];
    if (direct) {return direct;}
    var indirect;
    $(original).children().each (function (index) {
      if (!indirect) {
        var link = get_link (this);
        if (link) {
          indirect = connections_table [link.slice (1)];
        }
      }
    });
    return indirect;
  }
  function get_connections (element) {
    return get_tile_info (element).connections;
  }
   
  function get_icon (element) {
    var original = (typeof element === "string") && ('#'+element) || get_link (element);
    var indirect;
    $(original).children().each (function (index) {
      if (!indirect) {
        var link = get_link (this);
        if (link) {
          indirect = icons_table [link.slice (1)];
        }
      }
    });
    return indirect;
  }

  var icons_by_tile_id = {};
  var info_by_tile_id = {};

  tile_ids.forEach(function(id) {
    icons_by_tile_id[id] = get_icon(id);
    info_by_tile_id[id] = get_tile_info(id);
  });
  info_by_tile_id [blank_hex_id] = connections_table [blank_hex_id];
  
  
  
  
  function get_tile (tiles, location) {
    return tiles [position_string (location)]
  }
  function set_tile (tiles, tile) {
    tiles [position_string (tile)] = tile
  }
  function remove_tile (tiles, location) {
    delete tiles [position_string (location)]
  }

    
  function collect_path (tiles, tile, from_direction) {
    var found = {};
    var result = {components: [], icons: [], lock: false, completed: true};
    function find (tile, from_direction) {
      if (!tile) {result.completed = false; return;}
      if (!found [position_string (tile)+"_"+from_direction]) {
        found [position_string (tile)+"_"+from_direction] = true;
        var connections = info_by_tile_id[tile.tile_id].connections;
        var index = (from_direction + 6 - tile.rotation) % 6;
        var destination = connections[index];
        if (typeof destination === "number") {
          destination = (connections[index] + tile.rotation) % 6;
          found [position_string (tile)+"_"+destination] = true;
          var neighbor = get_tile (tiles, in_direction (tile, destination));
          find(neighbor, (destination + 3) % 6);
          result.components.push ({tile, from: from_direction, towards: destination});
        }
        else if (destination === "lock") {
          result.components.push ({tile, from: from_direction, towards: destination})
          result.lock = true;
          for (var direction = 0; direction <6 ;++direction) {
            if (connections [(direction + 6 - tile.rotation) % 6] == lock) {
              var neighbor = get_tile (tiles, in_direction (tile, direction));
              find(neighbor, (direction + 3) % 6);
            }
          }
        }
        else {
          result.components.push ({tile, from: from_direction, towards: destination});
          if (destination === icon) {result.icons.push (tile);}
        }
      }
    }
    find (tile, from_direction);
    find (get_tile (tiles, in_direction (tile, from_direction)), (from_direction + 3) % 6);
    return result;
  }
  
  function collect_paths (tiles, tile) {
    // TODO: no repeats
    var connections = info_by_tile_id[tile.tile_id].connections;
    var result = [];
    for (var direction = 0; direction <6 ;++direction) {
      result.push (collect_path (tiles, tile, direction));
    }
    return result;
  }
  
  function path_legality (path, placed_tile) {
    var forbidden = false;
    if (path.icons.length >1) {path.icons.forEach(function(tile) {
      if (tile === placed_tile) {forbidden = true;}
    });}
    if (forbidden) {return "forbidden";}
    
    if (!path.completed) {return "acceptable";}
    
    if (path.icons.length === 0) {return "acceptable";}
    if (path.icons.length === 1) {return "waste";}
    if (path_effects (path) === undefined) {return "waste";}
    
    return "success";
  }
  var legality_fill = {
    acceptable: "#0000ff",
    forbidden: "#ff0000",
    waste: "#990000",
    success: "#ffff00"
  };
  
  

  function neutral_transform (id) {
    var original = $("#"+id)[0];
    
    //does not take into account clipping paths
    var inaccurate_offset = original.getBBox();
    
    var offset = info_by_tile_id[id].offset;
    var icon = icons_by_tile_id[id];
    var offset_horizontal = offset.horizontal + (icon && icon.grid_position*1.732 || 0);
    var offset_vertical = 1052.36218-offset.vertical;
    
    //console.log (offset);
    var transform_origin = ""+(offset_horizontal)+"px "+(offset_vertical)+"px 0px"//"50% 50% 0";//""+ (offset.x+0.5*offset.width)+"px "+ (offset.y+0.5*offset.height)+"px 0px";
    //console.log (transform_origin);
    var transform = (
      //"translate("+ (-(offset.x+0.5*offset.width))+"px, "+ (-(offset.y+0.5*offset.height))+"px)"
      "translate("+ (-(offset_horizontal))+"px, "+ (-(offset_vertical))+"px)"
    );
    //console.log (transform);
    return {"transformOrigin": transform_origin, transform: transform}
  }
  function calculate_transform (id, horizontal, vertical, rotation) {
    var result = neutral_transform (id);
    
    var position = tile_position (horizontal, vertical);
    result.transform = result.transform + (
      " translate(" + position.horizontal + "px," + position.vertical + "px) rotate("+(-0.0833 + rotation/6)+"turn) scale(" + long_radius+ "," + long_radius+ ")"
    );
    //console.log (transform);
    return result
  }
  
  
  function create_random_tile (game_state) {
    var choose_icon = Math.random() < 0.8;
    var id;
    var player;
    while (true) {
      id = random_choice (tile_ids);
      var icon = icons_by_tile_id[id];
      var info = info_by_tile_id[id];
      
      //console.log(info.weight*(icon && icon.weight || 1));
      if ((!!icon === !!choose_icon) && (Math.random()*10000 < info.weight*(icon && icon.weight || 1))) {
        //hack: preserve the ratio of player-specific icons to non-player-specific icons, regardless of the number of players
        if (icon && icon.color && !player) {
          player = random_choice (game_state.players);
        }
        if (!(player && icon.color !== player.based_on)) {
          break;
        }
      }
    }
    var result = {tile_id: id, rotation: random_range (0, 6)};
    result.graphical_rotation = result.rotation;
    result.player = player;
    result.key = game_state.next_tile_key++;
    result.icon = icons_by_tile_id [result.tile_id];
    return result;
  }
  
  function new_tile(game_state) {
    var tile = create_random_tile(game_state);
    game_state.tiles.push (tile);
  }
  
  function begin_turn (state) {
    var current_player_index = (state.current_player.index + 1) % state.players.length;
    var old_player = state.current_player;
    var player = state.current_player = state.players [current_player_index];
    
    if (old_player.skip_turns >0) {
      old_player.skip_turns--;
    }
    if (player.skip_turns >0) {
      state.current_prompt = {
        kind: "message",
        message: "still_skipping",
      };
      return;
    }
    
    var tile = create_random_tile(state);
    
    if (tile.player === player && (tile.icon.icon === "torso" || tile.icon.icon === "crotch")) {
      state.current_prompt = {
        kind: "message",
        message: "tile_based_skipping",
        tile: tile,
      };
      return;
    }
    
    state.tiles.push (tile);
    state.current_prompt = {kind:"place_tile", tile: {...tile, key:"message_tile"}};
  }
  
  var messages = {
    still_skipping: function (state) {
      
    },
    tile_based_skipping: function (state) {
      
    },
  }
  
    
  var element = React.createElement;

  class Tile extends React.Component {
    render() {
      var CSS = calculate_transform (this.props.tile_id, this.props.horizontal, this.props.vertical, this.props.graphical_rotation);
      /*if (this.props.player) {
        CSS ["--icon-fill"] = this.props.player.fill;
        CSS ["--icon-stroke"] = this.props.player.stroke;
      }*/
      return element ("use", {xlinkHref: "#"+this.props.tile_id, x:0, y:0, className:"tile", style:CSS, onClick: this.props.onClick});
    }
    update_CSS_variables() {
      // Work around React not supporting CSS variables fully
      var that = this;
      var node = ReactDOM.findDOMNode (this);
      if (this.props.player) {
        node.style.setProperty ("--icon-fill", this.props.player.fill);
        node.style.setProperty ("--icon-stroke", this.props.player.stroke);
      }
      if (this.props.extra_CSS) {Object.getOwnPropertyNames (this.props.extra_CSS).forEach(function(prop) {
        node.style.setProperty (prop, that.props.extra_CSS[prop]);
      });}
    }
    componentDidMount() {
      this.update_CSS_variables() ;
    }
    componentDidUpdate() {
      this.update_CSS_variables() ;
    }
  }
  class Game extends React.Component {
    constructor (props) {
      super(props);
      this.state={
        tiles: [],
        tiles_by_location: {},
        next_tile_key: 0,
        players: props.players,
      };
      this.state.players.forEach(function(player, index) {
        player.index = index;
        player.skip_turns = 0;
      });
      while (!(this.state.tiles[0] && this.state.tiles[0].player)) {
        this.state.tiles = [];
        new_tile (this.state);
      }
      this.state.current_player = this.state.players [
        (this.state.players.length + this.state.tiles[0].player.index - 1)
        % this.state.players.length
      ];
      this.state.tiles [0].horizontal = 0;
      this.state.tiles [0].vertical = 0;
      set_tile (this.state.tiles_by_location, this.state.tiles [0]);
      begin_turn (this.state);
    }
    
    move_floating_tile(location) {
      var that = this;
      return function () {that.setState (function (state, props) {
        state = _.cloneDeep (state);
        var floating_tile = state.tiles [state.tiles.length - 1];
        
        if (floating_tile.horizontal !== undefined) {remove_tile (state.tiles_by_location, floating_tile) ;}
        floating_tile.horizontal = location.horizontal;
        floating_tile.vertical = location.vertical;
        set_tile (state.tiles_by_location, floating_tile);
        
        return state;
      });};
    }
    
    rotate_floating_tile(amount) {
      var that = this;
      return function () {that.setState (function (state, props) {
        state = _.cloneDeep (state);
        var floating_tile = state.tiles [state.tiles.length - 1];
        
        floating_tile.graphical_rotation += amount;
        floating_tile.rotation = (floating_tile.rotation + amount + 6) % 6;
        
        return state;
      });};
    }
    
    place_floating_tile() {
      var that = this;
      return function () {that.setState (function (state, props) {
        state = _.cloneDeep (state);
        var floating_tile = state.tiles [state.tiles.length - 1];
        
        begin_turn (state);
        
        return state;
      });}
    }
    
    dismiss_message() {
      var that = this;
      return function () {that.setState (function (state, props) {
        state = _.cloneDeep (state);
        
        begin_turn (state);
        
        return state;
      });}
    }

    
    render() {
      var tiles = [];
      var tile_metadata = {};
      var border_tiles = [];
      var border_tile_locations = {};
      var min_horizontal = 0;
      var max_horizontal = 0;
      var min_vertical = 0;
      var max_vertical = 0;
      var that = this;
      var floating_tile;
      if (this.state.current_prompt.kind === "place_tile") { floating_tile = this.state.tiles [this.state.tiles.length - 1];}
      function include (location) {
        var position = tile_position (location);
        min_horizontal = Math.min (min_horizontal, position.horizontal - long_radius);
        max_horizontal = Math.max(max_horizontal, position.horizontal + long_radius);
        min_vertical = Math.min (min_vertical , position.vertical - short_radius);
        max_vertical = Math.max(max_vertical , position.vertical + short_radius);
      }
      var clear_tile = function(tile) {
        var CSS = {};
        function do_connection (identifier) {
          CSS ["--path-fill-" + identifier] = "#808080";
        }
        info_by_tile_id[tile.tile_id].connections.forEach(function(connection, index) {
          if (typeof connection == "number") {
            if (index <connection) {
              do_connection (index + "-" + connection);
            }
          }
          else if (connection == "lock") {
            do_connection ("lock");
          } else {
            do_connection (index + "-" + connection);
          }
        });
        tile_metadata [tile.key] = {
          CSS: CSS,
        }
      }
      this.state.tiles.forEach(clear_tile);
      if (this.state.current_prompt.tile){ clear_tile (this.state.current_prompt.tile);}
      
      
      function fill_component (tile, from, towards, fill) {
    from = (from + 6 - tile.rotation) % 6;
    var CSS = tile_metadata [tile.key].CSS
    if (typeof towards === "number") {
      towards = (towards + 6 - tile.rotation) % 6 ;
      if (from >towards) {[from, towards] = [towards, from];}
      CSS ["--path-fill-" + from + "-" + towards]= fill;
    }
    else if (towards === lock) {
      CSS ["--path-fill-lock"]= fill;
    } else {
      CSS ["--path-fill-" + from + "-" + towards]= fill;
    }
  }
      if (floating_tile && floating_tile.horizontal !== undefined) {collect_paths (that.state.tiles_by_location, floating_tile).forEach(function(path) {
        var fill = legality_fill [path_legality (path, floating_tile)];
        path.components.forEach(function(component) {
          fill_component (component.tile, component.from, component.towards, fill);
        });
      });}
      
      var draw_tile = function(tile) {
        return element (Tile, {extra_CSS: tile_metadata [tile.key].CSS, ...tile});
      }
      var draw_standalone_tile = function (tile) {
        var modified = {...tile};
        modified.horizontal = 0; modified.vertical = 0;
        return element ("svg", {width: long_radius*2, height: short_radius*2, style:{display: "block", margin: "0.9em auto"}}, element ("g", {style: {transform: "translate("+long_radius+"px,"+short_radius+"px)"}}, draw_tile(modified)));
      }
      
      this.state.tiles.forEach(function(tile) {
        if (tile.horizontal === undefined) {return;}
        include (tile);
        tiles.push (draw_tile (tile));
        if (tile !== floating_tile) {for (var direction = 0; direction <6 ;++direction) {
          var neighbor = in_direction (tile, direction);
          var whatever = position_string (neighbor);
          if (!(get_tile (that.state.tiles_by_location, neighbor) || border_tile_locations [whatever])) {
            border_tile_locations [whatever] = true;
            include (neighbor);
            border_tiles.push (element (Tile, {key: whatever, horizontal: neighbor.horizontal, vertical: neighbor.vertical, tile_id: blank_hex_id, rotation: 0, graphical_rotation: 0, onClick: that.move_floating_tile (neighbor)}));
          }
        }}
      });
      var transform ="translate(" + (-min_horizontal) + "px, "+ (-min_vertical) + "px)";
      
      
      
      var board = element ("svg", {width: max_horizontal - min_horizontal, height: max_vertical - min_vertical, style:{display: "block", margin: "0 auto"}}, element ("g", {style: {transform}}, border_tiles, tiles));
      
      var message_props = {id: "messages", style:{
            backgroundColor: "#ffcccc",
            textAlign: "center",
            padding: "0.1em",
            fontSize: "120%",
          }};
      var message_children = [];
      var paragraph = function (text) {return element ("p", {}, text);};
      var player = this.state.current_player;
      var tile = this.state.current_prompt.tile;
      var icon = tile && tile.icon;
      message_children.push(paragraph (`${player.name}'s turn!`));
      
      if (this.state.current_prompt.tile) {
        message_children.push(paragraph (`${player.name}, you drew:`));
        message_children.push (draw_standalone_tile (this.state.current_prompt.tile));
      }
      
      if (this.state.current_prompt.kind === "place_tile") {
        var buttons = element ("div", {id: "tile_controls"},
          element ("button", {onClick: this.rotate_floating_tile (- 1)}, "rotate left"),
          element ("button", {onClick: this.rotate_floating_tile (1)}, "rotate right"),
          element ("button", {onClick: this.place_floating_tile()}, "place tile")
        );
        return element ("div", {}, element ("div", message_props, message_children), board, buttons);
      }
      else {
        var message = this.state.current_prompt.message;
        if (message === "tile_based_skipping") {
          message_children.push (paragraph (`Whoops! It's your own ${icon.icon}. You skip your turn.`));
          message_children.push (element ("button", {onClick: this.dismiss_message()}, "Drat"));
        }
        if (message === "still_skipping") {
          message_children.push (paragraph (`Whoops! You are still skipping turns.`));
          message_children.push (element ("button", {onClick: this.dismiss_message()}, "Drat"));
        }
        return element ("div", {}, element ("div", message_props, message_children), board);
      }
    }
  }
  

  ReactDOM.render(
    element (Game, {players: [
      {based_on: "white", name: "white", fill: "#ffffff", stroke: "#000000"},
      {based_on: "black", name: "black", fill: "#000000", stroke: "#ffffff"},
      /*{based_on: "white", name: "pink", fill: "#ffaaff", stroke: "#ff00ff"},
      {based_on: "white", name: "green", fill: "#99ff99", stroke: "#008800"},
      {based_on: "black", name: "blue", fill: "#0000ff", stroke: "#ffffff"},
      {based_on: "black", name: "purple", fill: "#5500aa", stroke: "#ffffff"},*/
    ]}),
    document.getElementById("content")
  );

}());
